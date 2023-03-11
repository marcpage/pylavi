.PHONE:clean venv install upgrade uninstall check dist format lint test

MODULE_NAME=pylavi
SOURCES=$(MODULE_NAME)/*.py
TESTS=tests/*.py
VENV_DIR=.venv
VENV_ACTIVATE_SCRIPT=$(VENV_DIR)/bin/activate
LINT_LOG=$(VENV_DIR)/lint.txt
BLACK_LOG=$(VENV_DIR)/format.txt
TEST_LOG=$(VENV_DIR)/test.txt
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
	-@$(RUN_IN_VENV) pip3 install -q black && black $(SOURCES) 2> $@
	@echo Source Formatted

format: $(BLACK_LOG)
	@cat $<

$(LINT_LOG): $(SOURCES) $(VENV_ACTIVATE_SCRIPT)
	-@$(RUN_IN_VENV) pip3 install -q pylint && pylint $(SOURCES) > $@
	@echo Linting Complete

lint: $(LINT_LOG) format
	@cat $<

$(TEST_LOG): $(SOURCES) $(TESTS)
	-@$(RUN_IN_VENV) pip3 install -q pytest && pytest > $@

test: $(TEST_LOG)
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

dist:
	python3 setup.py sdist
