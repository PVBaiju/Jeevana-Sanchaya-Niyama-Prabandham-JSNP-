from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout


class IncomePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Income Module")

        label.setAlignment(Qt.AlignCenter)

        label.setStyleSheet("font-size:24px;font-weight:bold;")

        layout.addStretch()

        layout.addWidget(label)

        layout.addStretch()

        self.setLayout(layout)