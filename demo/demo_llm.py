from app.services.llm_service import LLMService


service = LLMService()

result = service.generate_voice_package(

    action="Delete production database",

    priority="HIGH",

    decision="CALL_HUMAN",

    human_decision_index=100,

)

print("=" * 60)
print("SMARTESCALATE AI")
print("LLM DEMO")
print("=" * 60)

print()

print(result)