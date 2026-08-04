"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : application.py
Description    : Application Bootstrap
===============================================================================
"""

import sys

from PySide6.QtWidgets import QApplication

from app.main_window import MainWindow
from config.config_manager import ConfigManager
from core.logger import LoggerManager
from core.paths import PathManager


class SanchayamApplication:
    """
    Main Application Bootstrap Class.
    """

    def __init__(self) -> None:

        self.qt_app = QApplication(sys.argv)

        self.paths = None
        self.logger = None
        self.config = None
        self.window = None

    # ------------------------------------------------------------------

    def initialize(self) -> None:

        self.paths = PathManager()

        self.logger = LoggerManager.get_logger()

        self.config = ConfigManager()

        self.logger.info("=" * 70)
        self.logger.info("Starting Sanchayam...")
        self.logger.info("=" * 70)
        self.logger.info("Configuration Loaded Successfully")

    # ------------------------------------------------------------------

    def run(self) -> int:

        self.initialize()

        self.window = MainWindow()

        self.window.show()

        self.logger.info("Desktop UI Started")

        return self.qt_app.exec()