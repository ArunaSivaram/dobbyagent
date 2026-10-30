# CLAUDE.md — working conventions for this repo

This file tells Claude Code (and anyone pairing with it) how we work. Keep it
short. If a rule stops being true, change the rule.

## Config and secrets
- All config comes from environment variables.
- Env vars are read **only** in `src/dobby/config.py`. Everything else imports
  from `dobby.config`.
- Never commit secrets. Never print, log, or echo a secret value — not even
  truncated. If a value could be sensitive, redact it before logging.
- `.env` is gitignored; `.env.example` is the shared template.

## LLM calls
- Every model call goes through the provider-agnostic wrapper in
  `src/dobby/llm/`.
- The agent code never imports `anthropic` (or any provider SDK) directly.
- The wrapper logs token counts and estimated cost for every call.

## External services
- Any external service (LLM, calendar, search, DB) sits behind a small
  interface defined in this repo.
- Tests use fakes/stubs for those interfaces. **Tests never hit the network.**

## Code style
- Type hints on every public function.
- Prefer small functions. If a function doesn't fit on a screen, split it.
- Every module has at least one test.
- Run `make check` and make sure it's green before saying a task is done.

## Dependencies
- Ask before adding a new dependency. In the ask, say what it does, what the
  alternative is (including "write it ourselves"), and the maintenance cost.

## Learning mode (how to teach while building)
1. Before coding, explain the plan in plain English — what we're building and why.
2. Define each new technical term the first time it appears, once.
3. When there's a real choice to make, present 2 options with trade-offs. Don't
   pretend the choice is obvious when it isn't.
4. After coding, summarise the key concept the change exercised (1-2 sentences).
5. Warn before anything that costs money (real API calls) or touches production
   (deploys, writes to shared infra). Ask for explicit confirmation.
