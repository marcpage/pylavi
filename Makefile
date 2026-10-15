.PHONY:clean venv install upgrade uninstall check dist deploy format lint test coverage report
.DELETE_ON_ERROR:

MIN_TEST_COVERAGE=99
MODULE_NAME=pylavi
REQUIREMENTS_FILE=requirements.txt
INFRA_REQUIREMENTS_FILE=requirements-infra.txt
SOURCES=$(MODULE_NAME)/*.py
TEST_DIR=tests
TESTS=$(TEST_DIR)/*.py
TEST_FILES=$(TEST_DIR)/*.vi $(TEST_DIR)/*.yaml
VENV_DIR=.venv
VENV_ACTIVATE_SCRIPT=$(VENV_DIR)/bin/activate
LINT_LOG=$(VENV_DIR)/lint.txt
BLACK_LOG=$(VENV_DIR)/format.txt
TEST_LOG=$(VENV_DIR)/test.txt
DIST_LOG=$(VENV_DIR)/dist.txt
DEPLOY_LOG=$(VENV_DIR)/deploy.txt
COVERAGE_LOG=$(VENV_DIR)/coverage.txt
RUN_IN_VENV=. $(VENV_ACTIVATE_SCRIPT) &&
VERSION=$(shell sed -nE 's/^__version__ = "(.+)"/\1/p' $(MODULE_NAME)/__init__.py)
SETTINGS=$(VENV_DIR)/bin/python3 -m devopsdriver.manage_settings --script Makefile
PUBLISH_RETRY_SECONDS=10
# test_find_files scans the pylavi source directory, which a published package test does not have
# Passed in PYTEST_ADDOPTS since tests call parse_args([]), which falls back to sys.argv
PUBLISHED_TEST_ARGS=-q --rootdir=. --deselect $(TEST_DIR)/test_validate.py::test_find_files

# Upload dist/* using the repo, username, and password for $(1) in devopsdriver.yml
define upload
	@TWINE_USERNAME=`$(SETTINGS) $(1).username` TWINE_PASSWORD=`$(SETTINGS) $(1).password` \
		$(VENV_DIR)/bin/twine upload --non-interactive --repository `$(SETTINGS) $(1).repo` $(2) dist/*
endef

# Install the published package into a new venv in $(1) using pip index arguments $(2), then run the tests there
define test_published
	@rm -Rf $(1) && mkdir -p $(1) && cp -R $(TEST_DIR) $(1)/ && python3 -m venv $(1)/.venv
	@for attempt in 1 2 3 4 5 6; do \
		$(1)/.venv/bin/pip install -q --no-cache-dir $(2) $(MODULE_NAME)==$(VERSION) && exit 0; \
		echo "$(MODULE_NAME) $(VERSION) not available yet, retrying in $(PUBLISH_RETRY_SECONDS) seconds"; \
		sleep $(PUBLISH_RETRY_SECONDS); \
	done; exit 1
	@$(1)/.venv/bin/pip install -q $(MODULE_NAME)==$(VERSION) pytest
	@cd $(1) && PYTEST_ADDOPTS="$(PUBLISHED_TEST_ARGS)" .venv/bin/python -m pytest
endef

all:format lint coverage install check dist

clean:
	rm -Rf build dist $(MODULE_NAME).egg-info $(VENV_DIR) htmlcov .coverage .pytest_cache
	@echo Now Clean

$(VENV_ACTIVATE_SCRIPT):
	@python3 -m venv $(VENV_DIR)
	@$(RUN_IN_VENV) python3 -m pip install -q --upgrade pip && pip3 install -q setuptools wheel
	@$(RUN_IN_VENV) pip3 install -r $(REQUIREMENTS_FILE)
	@echo VENV Created

venv: $(VENV_ACTIVATE_SCRIPT)

$(BLACK_LOG): $(SOURCES) $(VENV_ACTIVATE_SCRIPT)
	@$(RUN_IN_VENV) pip3 install -q -r $(INFRA_REQUIREMENTS_FILE) && black $(SOURCES) \
		2> $@ || (cat $@; exit 1)
	@echo Source Formatted

format: $(BLACK_LOG)
	@cat $<

$(LINT_LOG): $(SOURCES) $(VENV_ACTIVATE_SCRIPT)
	@$(RUN_IN_VENV) pip3 install -q -r $(INFRA_REQUIREMENTS_FILE) && pylint $(SOURCES) \
		> $@ || (cat $@; exit 1)
	@$(RUN_IN_VENV) pip3 install -q -r $(INFRA_REQUIREMENTS_FILE) && black --check $(SOURCES) \
		2>> $@ || (cat $@; exit 1)
	@echo Linting Complete

lint: $(LINT_LOG)
	@cat $<

$(TEST_LOG): $(SOURCES) $(TESTS) $(TEST_FILES) $(VENV_ACTIVATE_SCRIPT)
	@$(RUN_IN_VENV) pip3 install -q -r $(INFRA_REQUIREMENTS_FILE) && coverage run --source=$(MODULE_NAME) -m pytest \
		> $@ || (cat $@; exit 1)

test: $(TEST_LOG)
	@cat $<

$(COVERAGE_LOG): $(TEST_LOG)
	@$(RUN_IN_VENV) coverage report --skip-covered --show-missing --fail-under=$(MIN_TEST_COVERAGE) \
		> $@ || (cat $@; exit 1)

report: $(TEST_LOG)
	@$(RUN_IN_VENV) coverage html --skip-covered
	@open htmlcov/index.html

coverage: $(COVERAGE_LOG)
	@cat $<

install: $(VENV_ACTIVATE_SCRIPT)
	$(RUN_IN_VENV) pip3 install .
	@echo $(MODULE_NAME) installed

upgrade: $(VENV_ACTIVATE_SCRIPT)
	$(RUN_IN_VENV) pip install --upgrade .
	@echo $(MODULE_NAME) upgraded

uninstall: $(VENV_ACTIVATE_SCRIPT)
	$(RUN_IN_VENV) pip uninstall $(MODULE_NAME) -y
	@echo $(MODULE_NAME) uninstalled

check: $(DIST_LOG)
	@$(RUN_IN_VENV) twine check --strict dist/*

$(DIST_LOG): $(SOURCES) README.md LICENSE setup.py $(VENV_ACTIVATE_SCRIPT)
	@rm -Rf build dist $(MODULE_NAME).egg-info
	@$(RUN_IN_VENV) pip3 install -q --upgrade build twine && python3 -m build > $@ || (cat $@; exit 1)
	@$(RUN_IN_VENV) twine check --strict dist/* >> $@ || (cat $@; exit 1)

dist: $(DIST_LOG)
	@cat $<

# Publishes to TestPyPI and tests it, then publishes to PyPI and tests that.
# Tokens come from the keychain entries named in devopsdriver.yml.
# To store them: .venv/bin/settings --secrets --script Makefile
$(DEPLOY_LOG): $(LINT_LOG) $(COVERAGE_LOG) $(DIST_LOG) devopsdriver.yml
	@grep --quiet "released&message=v$(VERSION)&" README.md || (echo "Update README.md badge to v$(VERSION)"; exit 1)
	@$(RUN_IN_VENV) pip3 install -q --upgrade twine devopsdriver
	@echo Uploading $(MODULE_NAME) $(VERSION) to test server
	$(call upload,pypi_test,--skip-existing)
	@echo Testing $(MODULE_NAME) $(VERSION) from test server
	$(call test_published,$(VENV_DIR)/test_published,--index-url `$(SETTINGS) pypi_test.url` --no-deps)
	@echo Uploading $(MODULE_NAME) $(VERSION) to production server
	$(call upload,pypi_prod)
	@echo Testing $(MODULE_NAME) $(VERSION) from production server
	$(call test_published,$(VENV_DIR)/prod_published,--index-url `$(SETTINGS) pypi_prod.url`)
	@echo $(MODULE_NAME) $(VERSION) published > $@
	@echo "Now tag the release: git tag v$(VERSION) && git push origin v$(VERSION)"

deploy: $(DEPLOY_LOG)
	@cat $<
