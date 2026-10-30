PTH_FILES := .venv/lib/python3.12/site-packages/*.pth

.PHONY: setup unhide test lint check eval run

setup:
	uv sync
	@$(MAKE) --no-print-directory unhide

unhide:
	@chflags nohidden $(PTH_FILES) 2>/dev/null || true

test: unhide
	uv run --no-sync pytest tests/ -v

lint: unhide
	uv run --no-sync ruff check

check: lint test

eval:
	@echo "eval harness not built yet (Module 2)"

run: unhide
	uv run --no-sync python $(ARGS)
