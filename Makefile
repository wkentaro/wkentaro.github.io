.PHONY: help setup lint format serve freeze
.DEFAULT_GOAL := help

help:  # Show this help
	@uv run --no-sync python -c "import re; lines=open('Makefile').read().splitlines(); print('\033[1;32mAvailable targets:\033[0m'); [print(f'  \033[1;36m{m.group(1):<10s}\033[0m {m.group(2)}') for l in lines if (m:=re.match(r'^([a-zA-Z_-]+):.*?# (.+)$$',l))]"

setup:  # Setup the development environment
	uv sync

lint:  # Lint code
	uv run ruff format --check
	uv run ruff check

format:  # Format code
	uv run ruff format
	uv run ruff check --fix

serve:  # Run the development server
	uv run ./runserver.py

freeze:  # Freeze the site into static HTML
	uv run ./freeze.py
