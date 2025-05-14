# Makefile
.DEFAULT_GOAL := help

.PHONY: install-hooks check lint format uninstall-hooks help

install-hooks:  ## Install all Python tools and register pre-commit Git hook
	pip install pre-commit black flake8 isort yamllint ansible-lint
	pre-commit install

check:  ## Run all checks (linting and formatting)
	pre-commit run --all-files

lint:  ## Run linting tools manually (flake8, yamllint, ansible-lint)
	flake8 .
	yamllint .
	ansible-lint .

format:  ## Run Python formatting tools manually (black, isort)
	black .
	isort .

uninstall-hooks:  ## Uninstall pre-commit hook from .git/hooks
	pre-commit uninstall

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-20s %s\n", $$1, $$2}'
