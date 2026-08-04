"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : application.py
Description    : Application Bootstrap
Author         : Baiju Nair
===============================================================================
"""

import sys
import models
from PySide6.QtWidgets import QApplication

from app.main_window import MainWindow
from config.config_manager import ConfigManager
from core.logger import LoggerManager
from core.paths import PathManager

# ========================= Database =========================
from database.base import Base
from database.database import engine
# ============================================================


class SanchayamApplication:
    """
    Main Application Bootstrap Class.
    Responsible for initializing the application and starting the UI.
    """

    def __init__(self) -> None:

        self.qt_app = QApplication(sys.argv)

        self.paths = None
        self.logger = None
        self.config = None
        self.window = None

    # =========================================================

    def initialize(self) -> None:
        """
        Initialize application components.
        """

        # Initialize folder structure
        self.paths = PathManager()

        # Initialize logger
        self.logger = LoggerManager.get_logger()

        self.logger.info("=" * 70)
        self.logger.info("Starting Sanchayam...")
        self.logger.info("=" * 70)

        # Load configuration
        self.config = ConfigManager()

        self.logger.info("Configuration Loaded Successfully")

        # Create all database tables
        Base.metadata.create_all(bind=engine)

        self.logger.info("Database Initialized Successfully")

        self.logger.info("Application Initialization Completed")

    # =========================================================

    def run(self) -> int:
        """
        Start the application.
        """

        self.initialize()

        self.window = MainWindow()

        self.window.show()

        self.logger.info("Desktop UI Started Successfully")

        return self.qt_app.exec()