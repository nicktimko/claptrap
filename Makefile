.PHONY: build test uploadtest upload

build:
	python setup.py sdist bdist_wheel

format:
	black .

test:
	# black --check .  # doesn't work in other versions
	pytest --cov=claptrap
	coverage report --show-missing
	coverage html

uploadtest:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	twine upload dist/*
