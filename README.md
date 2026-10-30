# dobby-agent

Dobby turns a pasted message with dates into Google Calendar events and sends
reminders. See `docs/PRD.md` for the full plan.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12.

```bash
uv sync
cp .env.example .env  # fill in ANTHROPIC_API_KEY
```

## Common tasks

```bash
make test    # run pytest
make lint    # run ruff
make check   # lint + test (run before saying a task is done)
make run ARGS='-m dobby'   # run the package
```

## Layout

- `src/dobby/` — the package
- `tests/` — pytest tests
- `docs/PRD.md` — product and technical plan
- `CLAUDE.md` — conventions for working in this repo
- `LEARNINGS.md` — per-module notes
