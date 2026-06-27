"""
Configuration for SmartEscalate AI

Loads environment variables and exposes application settings.
"""

from functools import lru_cache
import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "SmartEscalate AI"
    VERSION = "1.0.0"

    # -------------------------
    # OpenAI
    # -------------------------

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        ""
    )

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-4.1-mini"
    )

    TEMPERATURE = float(
        os.getenv(
            "TEMPERATURE",
            "0.2"
        )
    )

    MAX_TOKENS = int(
        os.getenv(
            "MAX_TOKENS",
            "700"
        )
    )

    # -------------------------
    # VocalBridge
    # -------------------------

    VOCALBRIDGE_API_KEY = os.getenv(
        "VOCALBRIDGE_API_KEY",
        ""
    )

    VOCALBRIDGE_AGENT_ID = os.getenv(
        "VOCALBRIDGE_AGENT_ID",
        ""
    )

    VOCALBRIDGE_API_URL = os.getenv(
        "VOCALBRIDGE_API_URL",
        "https://vocalbridgeai.com/api/v1/token"
    )

    # -------------------------
    # Frontend
    # -------------------------

    FRONTEND_URL = os.getenv(
        "FRONTEND_URL",
        "http://localhost:5173"
    )


@lru_cache
def get_settings():
    return Settings()