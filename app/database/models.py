"""
SmartEscalate AI Database Models

Stores all human approval requests
for audit and reporting.
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy.sql import func

from app.database.database import Base


class DecisionHistory(Base):
    """
    Stores every high-risk decision
    that required human approval.
    """

    __tablename__ = "decision_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    action = Column(
        String(300),
        nullable=False
    )

    reason = Column(
        Text,
        nullable=False
    )

    environment = Column(
        String(100),
        nullable=False
    )

    requested_by = Column(
        String(150),
        nullable=False
    )

    human_decision_index = Column(
        Integer,
        nullable=False
    )

    priority = Column(
        String(20),
        nullable=False
    )

    ai_decision = Column(
        String(50),
        nullable=False
    )

    human_response = Column(
        String(50),
        nullable=True,
        default="Pending"
    )

    summary = Column(
        Text,
        nullable=True
    )

    business_risk = Column(
        Text,
        nullable=True
    )

    priority_reason = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )