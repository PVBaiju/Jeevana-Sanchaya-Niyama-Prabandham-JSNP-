"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : base_repository.py
Description    : Generic Repository
===============================================================================
"""

from database.session import SessionLocal


class BaseRepository:
    """
    Base repository implementing common CRUD operations.
    """

    def __init__(self, model):

        self.model = model

    # ---------------------------------------------------------

    def get_all(self):

        with SessionLocal() as session:

            return session.query(self.model).all()

    # ---------------------------------------------------------

    def get_by_id(self, record_id):

        with SessionLocal() as session:

            return session.get(self.model, record_id)

    # ---------------------------------------------------------

    def add(self, entity):

        with SessionLocal() as session:

            session.add(entity)

            session.commit()

            session.refresh(entity)

            return entity

    # ---------------------------------------------------------

    def update(self):

        with SessionLocal() as session:

            session.commit()

    # ---------------------------------------------------------

    def delete(self, entity):

        with SessionLocal() as session:

            session.delete(entity)

            session.commit()