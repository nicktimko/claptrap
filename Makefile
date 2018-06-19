.PHONY: build test uploadtest upload

build:
	python setup.py sdist bdist_wheel

test:
	pytest --cov=claptrap

uploadtest:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	twine upload dist/*
