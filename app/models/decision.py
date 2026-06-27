from typing import Optional

from pydantic import BaseModel, Field


class DecisionRequest(BaseModel):
    """
    Request received from the frontend.

    This model describes the risky operation that
    SmartEscalate AI must analyze before deciding
    whether human approval is required.
    """

    # -----------------------------------
    # Business Context
    # -----------------------------------

    action: str = Field(
        ...,
        description="Risky action requested by the user."
    )

    reason: Optional[str] = Field(
        default="No reason provided.",
        description="Why this action is required."
    )

    environment: str = Field(
        default="Production",
        description="Development, Staging or Production."
    )

    requested_by: Optional[str] = Field(
        default="Unknown",
        description="Person or team requesting the action."
    )

    # -----------------------------------
    # Risk Signals
    # -----------------------------------

    destructive: bool = False

    production: bool = False

    security: bool = False

    customer_impact: bool = False

    business_preference: bool = False

    architecture_change: bool = False

    rollback_available: bool = True

    confidence: int = 100