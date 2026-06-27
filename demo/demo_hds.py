from app.core.hds_engine import HumanDecisionScore


engine = HumanDecisionScore()

score = engine.calculate(
    destructive=True,
    production=True,
    security=False,
    customer_impact=True,
    business_preference=True,
    architecture_change=False,
    rollback_available=False,
    confidence=35,
)

print(engine)