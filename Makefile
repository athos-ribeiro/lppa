.PHONY: clean devel check build

check:
	flake8 tests lppa
	coverage run --source=lppa -m pytest -v tests

coverage: check
	coverage report

devel:
	pip install -r requirements-dev.txt
	echo 'import setuptools; setuptools.setup()' > setup.py
	pip install -e .
	rm setup.py

clean:
	rm -rf *.egg-info dist build .pytest_cache */__pycache__ .coverage

build: clean
	python -m build
