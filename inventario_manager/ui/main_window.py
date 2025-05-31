from PySide6.QtWidgets import QMainWindow, QTabWidget
from ui.entrada_salida_tab import EntradaSalidaTab
from ui.lotes_tab import LotesTab
from ui.facturas_tab import FacturasTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Inventario")
        self.setGeometry(100, 100, 1024, 720)
        self.init_ui()

    def init_ui(self):
        tabs = QTabWidget()
        tabs.addTab(EntradaSalidaTab(), "Entrada / Salida")
        tabs.addTab(LotesTab(), "Lotes")
        tabs.addTab(FacturasTab(), "Facturas")
        self.setCentralWidget(tabs)
