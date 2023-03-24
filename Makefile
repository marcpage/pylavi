.PHONE:clean venv install upgrade uninstall check dist format lint test coverage report

MIN_TEST_COVERAGE=99
MODULE_NAME=pylavi
REQUIREMENTS_FILE=requirements.txt
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
COVERAGE_LOG=$(VENV_DIR)/coverage.txt
RUN_IN_VENV=. $(VENV_ACTIVATE_SCRIPT) &&

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
	@$(RUN_IN_VENV) pip3 install -q black && black $(SOURCES) \
		2> $@ || (cat $@; exit 1)
	@echo Source Formatted

format: $(BLACK_LOG)
	@cat $<

$(LINT_LOG): $(SOURCES) $(VENV_ACTIVATE_SCRIPT)
	@$(RUN_IN_VENV) pip3 install -q pylint && pylint $(SOURCES) \
		> $@ || (cat $@; exit 1)
	@$(RUN_IN_VENV) pip3 install -q black && black --check $(SOURCES) \
		2>> $@ || (cat $@; exit 1)
	@echo Linting Complete

lint: $(LINT_LOG)
	@cat $<

$(TEST_LOG): $(SOURCES) $(TESTS) $(TEST_FILES) $(VENV_ACTIVATE_SCRIPT)
	@$(RUN_IN_VENV) pip3 install -q pytest coverage && coverage run --source=$(MODULE_NAME) -m pytest \
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

check:
	python3 setup.py check

$(DIST_LOG): $(SOURCE) README.md LICENSE setup.py
	@mkdir -p $(VENV_DIR)
	@python3 setup.py sdist > $@ || (cat $@; exit 1)

dist: $(DIST_LOG)
	@cat $<
