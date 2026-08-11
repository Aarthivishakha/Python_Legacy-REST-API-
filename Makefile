.PHONY: test run analyze

test:
	python setup.py test

run:
	python run.py

analyze:
	python tool-triggers/scripts/run_beniget.py legacy_api
	python tool-triggers/scripts/run_pydriller.py .
