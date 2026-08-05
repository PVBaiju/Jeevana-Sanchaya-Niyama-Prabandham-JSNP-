"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : base_service.py
Description    : Base Service
===============================================================================
"""


class BaseService:
    """
    Base class for all business services.
    """

    def __init__(self, repository):

        self.repository = repository

    # ---------------------------------------------------------

    def get_all(self):

        return self.repository.get_all()

    # ---------------------------------------------------------

    def get_by_id(self, record_id):

        return self.repository.get_by_id(record_id)

    # ---------------------------------------------------------

    def save(self, entity):

        return self.repository.add(entity)

    # ---------------------------------------------------------

    def delete(self, entity):

        return self.repository.delete(entity)