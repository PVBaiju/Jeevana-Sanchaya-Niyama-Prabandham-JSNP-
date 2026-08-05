"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : payment_method.py
Description    : Payment Method Master
===============================================================================
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from models.base_entity import BaseEntity


class PaymentMethod(BaseEntity):

    __tablename__ = "master_payment_methods"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(250),
        default="",
    )

    icon: Mapped[str] = mapped_column(
        String(50),
        default="",
    )