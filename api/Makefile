dev:
	ENVIRONMENT_NAME=dev python main.py

test:
	ENVIRONMENT_NAME=test pytest -s

lint:
	find . -name "*.py" | xargs pylint

black:
	black --target-version=py39 .