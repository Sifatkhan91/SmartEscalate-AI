"""
SmartEscalate AI
LLM Service

Responsible for:
- Connecting to OpenAI
- Loading the system prompt
- Generating a structured VoicePackage
"""

from pathlib import Path
import logging

from openai import OpenAI

from app.core.config import get_settings
from app.models.voice_package import VoicePackage, VoiceOption


logger = logging.getLogger(__name__)


class LLMService:
    """
    OpenAI service responsible for generating
    AI-powered voice escalation packages.
    """

    def __init__(self):

        self.settings = get_settings()

        self.client = OpenAI(
            api_key=self.settings.OPENAI_API_KEY
        )

        self.system_prompt = self._load_prompt()

    def _load_prompt(self) -> str:
        """
        Load the system prompt from a text file.
        """

        prompt_path = (
            Path(__file__)
            .parent.parent
            / "templates"
            / "escalation_prompt.txt"
        )

        if prompt_path.exists():
            return prompt_path.read_text(
                encoding="utf-8"
            )

        logger.warning(
            "Prompt file not found. Using default prompt."
        )

        return """
You are SmartEscalate AI.

You are an Enterprise AI Governance Assistant.

Explain risky business and engineering actions
using clear language that executives can understand.

Keep responses concise.

Always return a valid VoicePackage.
"""

    def generate_voice_package(
        self,
        action: str,
        reason: str,
        environment: str,
        requested_by: str,
        priority: str,
        decision: str,
        human_decision_index: int,
    ) -> VoicePackage:
        """
        Generate an AI voice package.
        """

        user_prompt = f"""
Business Context

Requested By:
{requested_by}

Environment:
{environment}

Action:
{action}

Reason:
{reason}

Priority:
{priority}

Decision:
{decision}

Human Decision Index:
{human_decision_index}

Generate a professional executive voice briefing.

Do not simply repeat the input.

Explain:

1. What is happening.
2. Why it is risky.
3. Why human approval is required.
4. The two available options.
"""

        try:

            response = self.client.responses.parse(

                model=self.settings.OPENAI_MODEL,

                input=[
                    {
                        "role": "system",
                        "content": self.system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],

                text_format=VoicePackage,

            )

            logger.info(
                "Voice package generated successfully."
            )

            return response.output_parsed

        except Exception as e:

            logger.exception(
                "OpenAI request failed."
            )

            logger.exception(e)

            return VoicePackage(

                summary=action,

                business_risk="Unable to generate business explanation.",

                priority_reason="OpenAI service unavailable.",

                options=[

                    VoiceOption(
                        id=1,
                        title="Approve Operation",
                        risk="Proceed with the requested action.",
                    ),

                    VoiceOption(
                        id=2,
                        title="Cancel Operation",
                        risk="Stop execution.",
                    ),

                ],

                expected_reply="Approve Operation or Cancel Operation",

                voice_script=(
                    f"Hello. "
                    f"This is SmartEscalate AI. "
                    f"A {priority} priority decision "
                    f"requires your approval. "
                    f"The requested action is {action}. "
                    f"This request was submitted by {requested_by} "
                    f"for the {environment} environment."
                ),
            )