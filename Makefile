
setup:
	source ./.venv/bin/activate

run:
	uv run ostr

test:
	uv run pytest
