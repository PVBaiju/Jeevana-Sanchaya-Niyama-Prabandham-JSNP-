"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : base.py
Description    : SQLAlchemy Base Model
===============================================================================
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all ORM models.
    """
    pass