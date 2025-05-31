from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class LotesTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Control de Lotes"))
        self.setLayout(layout)
