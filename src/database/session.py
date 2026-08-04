"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : session.py
Description    : SQLAlchemy Session Manager
===============================================================================
"""

from sqlalchemy.orm import sessionmaker

from database.database import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)