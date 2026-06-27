"""
SmartEscalate AI
Database CRUD Operations

Handles:
1. Save Decision
2. Get Decision History
3. Update Human Response
"""

from sqlalchemy.orm import Session

from app.database.models import DecisionHistory


def save_decision(
    db: Session,
    action: str,
    reason: str,
    environment: str,
    requested_by: str,
    human_decision_index: int,
    priority: str,
    ai_decision: str,
    summary: str,
    business_risk: str,
    priority_reason: str,
):
    """
    Save a new decision to the database.
    """

    decision = DecisionHistory(

        action=action,

        reason=reason,

        environment=environment,

        requested_by=requested_by,

        human_decision_index=human_decision_index,

        priority=priority,

        ai_decision=ai_decision,

        summary=summary,

        business_risk=business_risk,

        priority_reason=priority_reason,

        human_response="Pending",

    )

    db.add(decision)

    db.commit()

    db.refresh(decision)

    return decision


def get_history(db: Session):
    """
    Return all previous decisions.
    """

    return (

        db.query(DecisionHistory)

        .order_by(
            DecisionHistory.created_at.desc()
        )

        .all()

    )


def get_decision(
    db: Session,
    decision_id: int,
):
    """
    Get one decision by ID.
    """

    return (

        db.query(DecisionHistory)

        .filter(
            DecisionHistory.id == decision_id
        )

        .first()

    )


def update_human_response(
    db: Session,
    decision_id: int,
    response: str,
):
    """
    Update Approve / Reject decision.
    """

    decision = get_decision(

        db,

        decision_id,

    )

    if decision is None:

        return None

    decision.human_response = response

    db.commit()

    db.refresh(decision)

    return decision