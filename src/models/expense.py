"""
===============================================================================
Expense Model
===============================================================================
"""

from datetime import date

from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models.base_entity import BaseEntity


class Expense(BaseEntity):

    __tablename__ = "expenses"

    expense_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("expense_categories.id"),
    )

    payment_method: Mapped[str] = mapped_column(
        String(50),
    )

    vendor: Mapped[str] = mapped_column(
        String(150),
        default="",
    )

    location: Mapped[str] = mapped_column(
        String(150),
        default="",
    )

    description: Mapped[str] = mapped_column(
        String(300),
        default="",
    )

    notes: Mapped[str] = mapped_column(
        String(500),
        default="",
    )

    receipt_path: Mapped[str] = mapped_column(
        String(300),
        default="",
    )

    category = relationship("ExpenseCategory")