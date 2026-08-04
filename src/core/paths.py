"""
===============================================================================
Project        : Sanchayam
Module         : Path Manager
Description    : Centralized Path Management

This module is responsible for:

1. Detecting the project root.
2. Creating required folders.
3. Providing commonly used application paths.
4. Supporting both Development and EXE modes.

===============================================================================
"""

from pathlib import Path
import sys

from core.constants import (
    DATABASE_FOLDER,
    LOG_FOLDER,
    EXPORT_FOLDER,
    BACKUP_FOLDER_PATH,
    ASSETS_FOLDER,
    DOCS_FOLDER,
    TEST_FOLDER,
)


class PathManager:
    """
    Centralized path management.

    All application modules should use this class
    instead of hardcoded paths.
    """

    def __init__(self) -> None:

        self.application_root = self._get_application_root()

        self.create_required_directories()

    # -------------------------------------------------------------------------

    def _get_application_root(self) -> Path:
        """
        Returns the application root directory.

        Development:
            Project Folder

        Production:
            EXE Folder
        """

        if getattr(sys, "frozen", False):
            return Path(sys.executable).parent

        return Path(__file__).resolve().parents[2]

    # -------------------------------------------------------------------------

    def create_required_directories(self) -> None:
        """
        Creates all required application folders.
        """

        folders = [
            DATABASE_FOLDER,
            LOG_FOLDER,
            EXPORT_FOLDER,
            BACKUP_FOLDER_PATH,
            ASSETS_FOLDER,
            DOCS_FOLDER,
            TEST_FOLDER,
        ]

        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)

    # -------------------------------------------------------------------------

    @property
    def database_path(self) -> Path:
        return DATABASE_FOLDER

    @property
    def log_path(self) -> Path:
        return LOG_FOLDER

    @property
    def export_path(self) -> Path:
        return EXPORT_FOLDER

    @property
    def backup_path(self) -> Path:
        return BACKUP_FOLDER_PATH