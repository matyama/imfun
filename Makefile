.PHONY: check fmt lint tests

setup:
	poetry env use python3.8
	poetry install
	poetry run pre-commit install

fmt:
	isort .
	black .

lint:
	flakehell lint
	MYPYPATH=imfun mypy .

tests:
	PYTHONPATH=imfun pytest

check: lint tests
