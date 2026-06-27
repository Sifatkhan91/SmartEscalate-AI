"""
SmartEscalate AI
Decision Service

Responsibilities:
1. Calculate the Human Decision Index (HDI)
2. Decide whether human escalation is required
3. Generate an AI voice package
"""

from app.core.hds_engine import HumanDecisionScore
from app.services.llm_service import LLMService


class DecisionService:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, request):

        # -----------------------------
        # Calculate Human Decision Index
        # -----------------------------
        engine = HumanDecisionScore()

        score = engine.calculate(
            destructive=request.destructive,
            production=request.production,
            security=request.security,
            customer_impact=request.customer_impact,
            business_preference=request.business_preference,
            architecture_change=request.architecture_change,
            rollback_available=request.rollback_available,
            confidence=request.confidence,
        )

        decision = engine.decision()

        # -----------------------------
        # Determine Priority
        # -----------------------------
        if score >= 80:
            priority = "HIGH"
        elif score >= 50:
            priority = "MEDIUM"
        else:
            priority = "LOW"

        # -----------------------------
        # No escalation required
        # -----------------------------
        if decision != "CALL_HUMAN":

            return {
                "action": request.action,
                "reason": request.reason,
                "environment": request.environment,
                "requested_by": request.requested_by,
                "human_decision_index": score,
                "decision": decision,
                "priority": priority,
                "requires_human": False,
                "voice_package": None,
            }

        # -----------------------------
        # Generate AI Voice Package
        # -----------------------------
        voice_package = self.llm.generate_voice_package(
            action=request.action,
            reason=request.reason,
            environment=request.environment,
            requested_by=request.requested_by,
            priority=priority,
            decision=decision,
            human_decision_index=score,
        )

        # -----------------------------
        # Final API Response
        # -----------------------------
        return {
            "action": request.action,
            "reason": request.reason,
            "environment": request.environment,
            "requested_by": request.requested_by,
            "human_decision_index": score,
            "decision": decision,
            "priority": priority,
            "requires_human": True,
            "voice_package": voice_package.model_dump(),
        }