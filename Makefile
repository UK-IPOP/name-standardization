# This file provides commonly used commands in an easy to run manner

format:
	@echo "Running black formatter..."
	@black src/standard_names
	@echo "Running isort formatter..."
	@isort src/standard_names

lint:
	@echo "Running flake8 linter..."
	@flake8 src/standard_names --max-line-length=89

docs:
	@echo "Making docs..."
	# do mkdocs stuff here

deploy-docs:
	@echo "Deploying docs..."
	# do mkdocs deploy here...