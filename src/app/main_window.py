"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : main_window.py
Description    : Main Desktop Window
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QMainWindow,
    QSplitter,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sanchayam - Personal Life Management System")
        self.resize(1400, 850)

        self.create_menu()
        self.create_toolbar()
        self.create_central_widget()
        self.create_statusbar()

    # ------------------------------------------------------------------

    def create_menu(self):

        menu_bar = self.menuBar()

        menu_bar.addMenu("File")
        menu_bar.addMenu("Finance")
        menu_bar.addMenu("Planner")
        menu_bar.addMenu("Reports")
        menu_bar.addMenu("Tools")
        menu_bar.addMenu("Help")

    # ------------------------------------------------------------------

    def create_toolbar(self):

        toolbar = QToolBar("Main Toolbar")

        self.addToolBar(toolbar)

    # ------------------------------------------------------------------

    def create_central_widget(self):

        splitter = QSplitter(Qt.Horizontal)

        navigation = QListWidget()

        navigation.addItems(
            [
                "🏠 Dashboard",
                "💰 Expenses",
                "💵 Income",
                "📅 Calendar",
                "📝 Journal",
                "📂 Documents",
                "🌾 Farm",
                "❤️ Health",
                "📊 Reports",
                "⚙ Settings",
            ]
        )

        navigation.setMaximumWidth(250)

        center = QWidget()

        layout = QVBoxLayout(center)

        title = QLabel("Welcome to Sanchayam")

        title.setStyleSheet(
            """
            font-size:24px;
            font-weight:bold;
            """
        )

        subtitle = QLabel(
            "Personal Life Management System\nVersion 0.1.0"
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()

        splitter.addWidget(navigation)
        splitter.addWidget(center)

        splitter.setStretchFactor(1, 1)

        self.setCentralWidget(splitter)

    # ------------------------------------------------------------------

    def create_statusbar(self):

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)