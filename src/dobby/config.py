"""All settings come from environment variables, read in one place."""
import os

from dotenv import load_dotenv

load_dotenv()  # copies values from .env into the environment, if the file exists

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "anthropic")
LLM_MODEL = os.getenv("LLM_MODEL", "claude-haiku-4-5-20251001")
TIMEZONE = os.getenv("TIMEZONE", "Asia/Singapore")
