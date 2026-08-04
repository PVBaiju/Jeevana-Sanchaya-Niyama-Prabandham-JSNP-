from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Dashboard")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        subtitle = QLabel(
            "Welcome to Sanchayam\n\nPersonal Life Management System"
        )

        subtitle.setAlignment(Qt.AlignCenter)

        layout.addStretch()

        layout.addWidget(title)

        layout.addWidget(subtitle)

        layout.addStretch()

        self.setLayout(layout)