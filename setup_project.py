import os

project = {
    "inventario_manager": {
        "config": {
            "settings.py": '''# Aquí va la configuración inicial del proyecto, por ahora sin conexión a base de datos
'''
        },
        "ui": {
            "__init__.py": "",
            "main_window.py": '''from PySide6.QtWidgets import QMainWindow, QTabWidget
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
''',
            "entrada_salida_tab.py": '''from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class EntradaSalidaTab(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Formulario Entrada / Salida")
        
        layout = QVBoxLayout()

        # Etiqueta y campo para Producto
        self.producto_label = QLabel("Producto ID:")
        self.producto_input = QLineEdit()
        layout.addWidget(self.producto_label)
        layout.addWidget(self.producto_input)

        # Etiqueta y campo para Cantidad
        self.cantidad_label = QLabel("Cantidad:")
        self.cantidad_input = QLineEdit()
        layout.addWidget(self.cantidad_label)
        layout.addWidget(self.cantidad_input)

        # Botones
        self.guardar_button = QPushButton("Guardar")
        self.limpiar_button = QPushButton("Limpiar")

        # Conectar señales de botones
        self.guardar_button.clicked.connect(self.guardar_datos)
        self.limpiar_button.clicked.connect(self.limpiar_campos)

        layout.addWidget(self.guardar_button)
        layout.addWidget(self.limpiar_button)

        self.setLayout(layout)

    def guardar_datos(self):
        # Aquí se iría la lógica para guardar los datos (por ahora solo un print)
        producto = self.producto_input.text()
        cantidad = self.cantidad_input.text()
        print(f"Guardando Producto: {producto}, Cantidad: {cantidad}")
    
    def limpiar_campos(self):
        self.producto_input.clear()
        self.cantidad_input.clear()
        print("Campos limpiados")
''',
            "lotes_tab.py": '''from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class LotesTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Control de Lotes"))
        self.setLayout(layout)
''',
            "facturas_tab.py": '''from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class FacturasTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Gestión de Facturas"))
        self.setLayout(layout)
''',
        },
        "db": {
            "__init__.py": "",
            "connection.py": "",  # Por ahora no necesitamos esta parte
        },
        "models": {
            "entrada_salida.py": "",  # Sin interacción con base de datos
            "lote.py": "",
            "factura.py": "",
        },
        "reports": {
            "pdf_report.py": "",
        },
        "assets": {},
        "docs": {
            "manual_usuario.pdf": None
        },
        "README.md": "# Sistema de Inventario PySide6 + Access",
        "main.py": '''import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
'''
    },
    "requirements.txt": "PySide6\n"
}

def create_structure(base, structure):
    for name, content in structure.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif content is None:
            open(path, 'wb').close()  # PDF simulado
        else:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    create_structure(".", project)
    print("✅ Proyecto reiniciado. Ahora puedes trabajar en la interactividad del formulario.")