"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : main_window.py
Description    : Main Application Window
===============================================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QListWidget,
    QMainWindow,
    QSplitter,
    QStackedWidget,
    QStatusBar,
    QToolBar,
)

from app.pages.dashboard_page import DashboardPage
from app.pages.expense_page import ExpensePage
from app.pages.income_page import IncomePage
from app.pages.calendar_page import CalendarPage
from app.pages.journal_page import JournalPage
from app.pages.report_page import ReportPage
from app.pages.farm_page import FarmPage
from app.pages.settings_page import SettingsPage


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Sanchayam - Personal Life Management System")
        self.resize(1450, 850)

        self.create_menu()
        self.create_toolbar()
        self.create_ui()
        self.create_statusbar()

    # -----------------------------------------------------------------

    def create_menu(self):

        menu = self.menuBar()

        menu.addMenu("File")
        menu.addMenu("Finance")
        menu.addMenu("Planner")
        menu.addMenu("Reports")
        menu.addMenu("Tools")
        menu.addMenu("Help")

    # -----------------------------------------------------------------

    def create_toolbar(self):

        toolbar = QToolBar()

        self.addToolBar(toolbar)

    # -----------------------------------------------------------------

    def create_ui(self):

        splitter = QSplitter(Qt.Horizontal)

        self.navigation = QListWidget()

        self.navigation.addItems([
            "🏠 Dashboard",
            "💰 Expenses",
            "💵 Income",
            "📅 Calendar",
            "📖 Journal",
            "📊 Reports",
            "🌾 Farm",
            "⚙ Settings"
        ])

        self.navigation.setMaximumWidth(230)

        self.pages = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.expense_page = ExpensePage()
        self.income_page = IncomePage()
        self.calendar_page = CalendarPage()
        self.journal_page = JournalPage()
        self.report_page = ReportPage()
        self.farm_page = FarmPage()
        self.settings_page = SettingsPage()

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.expense_page)
        self.pages.addWidget(self.income_page)
        self.pages.addWidget(self.calendar_page)
        self.pages.addWidget(self.journal_page)
        self.pages.addWidget(self.report_page)
        self.pages.addWidget(self.farm_page)
        self.pages.addWidget(self.settings_page)

        self.navigation.currentRowChanged.connect(
            self.pages.setCurrentIndex
        )

        self.navigation.setCurrentRow(0)

        splitter.addWidget(self.navigation)
        splitter.addWidget(self.pages)

        splitter.setStretchFactor(1, 1)

        self.setCentralWidget(splitter)

    # -----------------------------------------------------------------

    def create_statusbar(self):

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)