.PHONY: test

deps:
	pip install -r test_requirements.txt

lint:
	flake8 test

test:
	PYTHONPATH=. py.test --verbose -s --html=report.html
