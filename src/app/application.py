"""
=========================================================
Application Bootstrap
=========================================================
"""

import sys

from PySide6.QtWidgets import QApplication

from app.main_window import MainWindow


class Application:
    """
    Starts the Desktop Application
    """

    def __init__(self):

        self.qt_app = QApplication(sys.argv)

        self.window = MainWindow()

    def run(self):

        self.window.show()

        sys.exit(self.qt_app.exec())