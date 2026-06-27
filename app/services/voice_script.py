class VoiceScriptGenerator:

    def generate(
        self,
        priority: str,
        summary: str,
        impact: str,
        options,
        expected_reply: str,
    ):

        script = f"""
Hello.

This is SmartEscalate AI.

Priority level: {priority}.

{summary}

Business impact:

{impact}

You have two options.

Option One.

{options[0]["title"]}

Risk:

{options[0]["risk"]}

Option Two.

{options[1]["title"]}

Risk:

{options[1]["risk"]}

Please reply with:

{expected_reply}

Thank you.
"""

        return script.strip()