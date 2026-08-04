"""
=========================================================
Main Window
=========================================================
"""

from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from core.constants import (
    APP_NAME,
    PROJECT_CODE,
    VERSION,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)


class MainWindow(QMainWindow):
    """
    Main Application Window
    """

    def __init__(self):
        super().__init__()

        self.initialize_window()

    def initialize_window(self):

        self.setWindowTitle(APP_NAME)

        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )

        central_widget = QWidget()

        layout = QVBoxLayout()

        title = QLabel(f"🌿 {APP_NAME}")

        title.setStyleSheet("""
            font-size:32px;
            font-weight:bold;
            padding:20px;
        """)

        subtitle = QLabel(
            f"""
Personal Life Management System

Project Code : {PROJECT_CODE}

Version : {VERSION}
"""
        )

        subtitle.setStyleSheet("""
            font-size:18px;
            padding-left:20px;
        """)

        layout.addWidget(title)

        layout.addWidget(subtitle)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)