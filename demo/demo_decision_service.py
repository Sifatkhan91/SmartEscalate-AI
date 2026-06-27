"""
Demo for DecisionService
"""

from app.models.decision import DecisionRequest
from app.services.decision_service import DecisionService


service = DecisionService()

request = DecisionRequest(
    action="Delete production database",
    destructive=True,
    production=True,
    security=False,
    customer_impact=True,
    business_preference=True,
    architecture_change=False,
    rollback_available=False,
    confidence=35,
)

result = service.analyze(request)

print("=" * 70)
print("SMARTESCALATE AI")
print("DECISION SERVICE DEMO")
print("=" * 70)

print()

print(result)