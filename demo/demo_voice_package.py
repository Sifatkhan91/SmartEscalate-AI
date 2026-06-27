"""
Demo for VoicePackage model.
"""

from app.models.voice_package import VoicePackage, VoiceOption


voice_package = VoicePackage(
    summary="Deleting the production database may permanently remove customer records.",

    business_risk="Customer information could be permanently lost.",

    priority_reason="This action affects the production environment and cannot be undone.",

    options=[
        VoiceOption(
            id=1,
            title="Delete Database",
            risk="Permanent data loss",
        ),
        VoiceOption(
            id=2,
            title="Cancel Operation",
            risk="Deployment delayed",
        ),
    ],

    expected_reply="Delete Database or Cancel Operation",

    voice_script="""
Hello Sifat.

This is SmartEscalate AI.

A HIGH priority decision requires your approval.

Deleting this production database may permanently remove customer records.

Option One.

Delete Database.

Risk:

Permanent data loss.

Option Two.

Cancel Operation.

Risk:

Deployment delayed.

Please reply:

Delete Database

or

Cancel Operation.
""",
)

print("=" * 60)
print("SMARTESCALATE AI")
print("VOICE PACKAGE DEMO")
print("=" * 60)

print("\nStructured Object\n")

print(voice_package)

print("\n\nJSON Output\n")

print(voice_package.model_dump_json(indent=4))