.PHONE:clean venv install upgrade uninstall check dist format lint test coverage

MIN_TEST_COVERAGE=57
MODULE_NAME=pylavi
SOURCES=$(MODULE_NAME)/*.py
TEST_DIR=tests
TESTS=$(TEST_DIR)/*.py
VENV_DIR=.venv
VENV_ACTIVATE_SCRIPT=$(VENV_DIR)/bin/activate
LINT_LOG=$(VENV_DIR)/lint.txt
BLACK_LOG=$(VENV_DIR)/format.txt
TEST_LOG=$(VENV_DIR)/test.txt
COVERAGE_LOG=$(VENV_DIR)/coverage.txt
RUN_IN_VENV=. $(VENV_ACTIVATE_SCRIPT) &&

clean:
	@rm -Rf build dist $(MODULE_NAME).egg-info $(VENV_DIR)
	@echo Now Clean

$(VENV_ACTIVATE_SCRIPT):
	@python3 -m venv $(VENV_DIR)
	@$(RUN_IN_VENV) python3 -m pip install -q --upgrade pip && pip3 install -q setuptools wheel
	@echo VENV Created

venv: $(VENV_ACTIVATE_SCRIPT)

$(BLACK_LOG): $(SOURCES) $(VENV_ACTIVATE_SCRIPT)
	@$(RUN_IN_VENV) pip3 install -q black && black $(SOURCES) 2> $@
	@echo Source Formatted

format: $(BLACK_LOG)
	@cat $<

$(LINT_LOG): $(SOURCES) $(VENV_ACTIVATE_SCRIPT)
	@$(RUN_IN_VENV) pip3 install -q pylint && pylint $(SOURCES) > $@
	@echo Linting Complete

lint: $(LINT_LOG) format
	@cat $<

$(TEST_LOG): $(SOURCES) $(TESTS)  $(VENV_ACTIVATE_SCRIPT)
	@$(RUN_IN_VENV) pip3 install -q pytest coverage && coverage run -m pytest > $@

test: $(TEST_LOG)
	@cat $<

$(COVERAGE_LOG): $(TEST_LOG)
	@$(RUN_IN_VENV) coverage report --include="$(SOURCES)" --skip-covered > $@
	@$(RUN_IN_VENV) coverage html --include="$(SOURCES)" --skip-covered --fail-under=$(MIN_TEST_COVERAGE)

coverage: $(COVERAGE_LOG)
	@cat $<
	@open htmlcov/index.html

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

dist:
	python3 setup.py sdist
