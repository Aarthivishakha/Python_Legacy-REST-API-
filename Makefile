.PHONY: test run analyze

test:
	python setup.py test

run:
	python run.py

analyze:
	python tool-triggers/beniget/run_beniget.py legacy_api
	python tool-triggers/pydriller/run_pydriller.py .
