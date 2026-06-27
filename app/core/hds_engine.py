"""
Human Decision Score (HDS) Engine

This module determines whether an AI coding assistant
should interrupt a human by assigning a score
to the current situation.

Author: Sifat Ullah Khan
Project: SmartEscalate AI
"""


class HumanDecisionScore:

    def __init__(self):
        self.score = 0

    def calculate(
        self,
        destructive=False,
        production=False,
        security=False,
        customer_impact=False,
        business_preference=False,
        architecture_change=False,
        rollback_available=True,
        confidence=100,
    ):

        score = 0

        if destructive:
            score += 30

        if production:
            score += 25

        if security:
            score += 20

        if customer_impact:
            score += 20

        if business_preference:
            score += 20

        if architecture_change:
            score += 15

        if rollback_available:
            score -= 15

        if confidence >= 90:
            score -= 20
        elif confidence >= 75:
            score -= 10
        elif confidence <= 40:
            score += 20

        score = max(0, min(score, 100))

        self.score = score

        return score

    def decision(self):

        if self.score <= 30:
            return "AUTONOMOUS"

        elif self.score <= 60:
            return "REASON_AGAIN"

        else:
            return "CALL_HUMAN"

    def __str__(self):
        return f"HDS Score: {self.score} | Decision: {self.decision()}"