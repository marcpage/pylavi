.PHONE:clean venv install upgrade uninstall check dist format lint

clean:
	rm -Rf build dist pylavi.egg-info .venv

.venv/bin/activate:
	python3 -m venv .venv
	. .venv/bin/activate && \
		python3 -m pip install --upgrade pip && \
		pip3 install setuptools && \
		pip3 install wheel

venv: .venv/bin/activate

.venv/format.txt: pylavi/*.py .venv/bin/activate
	-@. .venv/bin/activate && \
		pip3 install -q black && \
		black pylavi/*.py 2> $@

format: .venv/format.txt
	@cat $<

.venv/lint.txt: pylavi/*.py .venv/bin/activate
	-@. .venv/bin/activate && \
		pip3 install -q pylint && \
		pylint pylavi/*.py > $@

lint: .venv/lint.txt format
	@cat $<

install: venv
	python3 -m venv .venv
	. .venv/bin/activate && \
		pip3 install .

upgrade: venv
	python3 -m venv .venv
	. .venv/bin/activate && \
		pip install --upgrade .

uninstall: venv
	python3 -m venv .venv
	. .venv/bin/activate && \
		pip uninstall pylavi -y

check:
	python3 setup.py check

dist:
	python3 setup.py sdist
