"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : expense_service.py
Description    : Expense Business Logic
===============================================================================
"""

from datetime import date

from models.expense import Expense
from repositories.expense_repository import ExpenseRepository
from services.base_service import BaseService


class ExpenseService(BaseService):

    def __init__(self):

        super().__init__(ExpenseRepository())

    # ---------------------------------------------------------

    def create_expense(
        self,
        expense_date: date,
        amount: float,
        category_id: int,
        payment_method_id: int,
        vendor: str = "",
        location: str = "",
        description: str = "",
        notes: str = "",
        receipt_path: str = "",
    ) -> Expense:

        # ----------------------------
        # Validation
        # ----------------------------

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if category_id <= 0:
            raise ValueError("Invalid Expense Category.")

        if payment_method_id <= 0:
            raise ValueError("Invalid Payment Method.")

        expense = Expense(

            expense_date=expense_date,

            amount=amount,

            category_id=category_id,

            payment_method_id=payment_method_id,

            vendor=vendor,

            location=location,

            description=description,

            notes=notes,

            receipt_path=receipt_path,

        )

        return self.save(expense)