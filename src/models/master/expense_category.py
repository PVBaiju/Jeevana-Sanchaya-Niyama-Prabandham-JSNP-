"""
===============================================================================
Expense Category Model
===============================================================================
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from models.base_entity import BaseEntity


class ExpenseCategory(BaseEntity):

    __tablename__ = "expense_categories"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    icon: Mapped[str] = mapped_column(
        String(50),
        default="",
    )

    color: Mapped[str] = mapped_column(
        String(20),
        default="#3B82F6",
    )

    description: Mapped[str] = mapped_column(
        String(250),
        default="",
    )