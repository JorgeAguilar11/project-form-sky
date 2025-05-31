from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

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
