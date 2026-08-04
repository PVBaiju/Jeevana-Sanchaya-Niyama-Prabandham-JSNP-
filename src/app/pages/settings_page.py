from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel


class SettingsPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Settings Module")

        label.setAlignment(Qt.AlignCenter)

        label.setStyleSheet("font-size:24px;font-weight:bold;")

        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()

        self.setLayout(layout)