from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class FacturasTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Gestión de Facturas"))
        self.setLayout(layout)
