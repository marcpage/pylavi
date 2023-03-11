.PHONE:clean venv install upgrade uninstall check dist format lint

SOURCES=pylavi/*.py

clean:
	rm -Rf build dist pylavi.egg-info .venv

.venv/bin/activate:
	@python3 -m venv .venv
	@. .venv/bin/activate && \
		python3 -m pip install -q --upgrade pip && \
		pip3 install -q setuptools && \
		pip3 install -q wheel

venv: .venv/bin/activate

.venv/format.txt: $(SOURCES) .venv/bin/activate
	-@. .venv/bin/activate && \
		pip3 install -q black && \
		black $(SOURCES) 2> $@

format: .venv/format.txt
	@cat $<

.venv/lint.txt: $(SOURCES) .venv/bin/activate
	-@. .venv/bin/activate && \
		pip3 install -q pylint && \
		pylint $(SOURCES) > $@

lint: .venv/lint.txt format
	@cat $<

install: venv
	. .venv/bin/activate && \
		pip3 install .

upgrade: venv
	. .venv/bin/activate && \
		pip install --upgrade .

uninstall: venv
	. .venv/bin/activate && \
		pip uninstall pylavi -y

check:
	python3 setup.py check

dist:
	python3 setup.py sdist
