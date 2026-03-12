.PHONY: install dev lint test

install:
pip install -e .

dev:
uvicorn terminalforge.main:app --reload

lint:
black .
isort .

format:
black .
isort .

format:
pytest
