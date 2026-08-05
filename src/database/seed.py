"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : seed.py
Description    : Database Seeder
===============================================================================
"""

from database.session import SessionLocal

from models.expense_category import ExpenseCategory
from models.master.payment_method import PaymentMethod


class DatabaseSeeder:

    @staticmethod
    def seed():

        session = SessionLocal()

        try:

            # ---------------------------------------------------------
            # Payment Methods
            # ---------------------------------------------------------

            if session.query(PaymentMethod).count() == 0:

                methods = [
                    "Cash",
                    "UPI",
                    "Bank Transfer",
                    "Credit Card",
                    "Debit Card",
                    "Cheque",
                    "Wallet",
                ]

                for method in methods:

                    session.add(
                        PaymentMethod(
                            name=method
                        )
                    )

            # ---------------------------------------------------------
            # Expense Categories
            # ---------------------------------------------------------

            if session.query(ExpenseCategory).count() == 0:

                categories = [

                    "Food",
                    "Fuel",
                    "Rent",
                    "Medical",
                    "Temple",
                    "Donation",
                    "Travel",
                    "Education",
                    "Groceries",
                    "Utilities",
                    "Farm",
                    "Entertainment",

                ]

                for category in categories:

                    session.add(
                        ExpenseCategory(
                            name=category
                        )
                    )

            session.commit()

        finally:

            session.close()