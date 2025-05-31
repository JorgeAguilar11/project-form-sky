from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QDateEdit, QTextEdit, QHBoxLayout, QApplication
)
import sys

class EntradaSalidaTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movimiento de Inventario")
        layout = QVBoxLayout()

        # Producto y Descripción
        layout.addWidget(QLabel("Producto:"))
        self.producto_input = QLineEdit()
        layout.addWidget(self.producto_input)

        layout.addWidget(QLabel("Descripción:"))
        self.descripcion_input = QLineEdit()
        layout.addWidget(self.descripcion_input)

        # Lote y Cantidad
        layout.addWidget(QLabel("Lote:"))
        self.lote_input = QLineEdit()
        layout.addWidget(self.lote_input)

        layout.addWidget(QLabel("Cantidad:"))
        self.cantidad_input = QLineEdit()
        layout.addWidget(self.cantidad_input)

        # Unidad y Tipo
        layout.addWidget(QLabel("Unidad:"))
        self.unidad_combo = QComboBox()
        self.unidad_combo.addItems(["Unidad", "Caja", "Kg", "Litro"])
        layout.addWidget(self.unidad_combo)

        layout.addWidget(QLabel("Tipo:"))
        self.tipo_combo = QComboBox()
        self.tipo_combo.addItems(["Entrada", "Salida"])
        layout.addWidget(self.tipo_combo)

        # Fecha de movimiento y vencimiento
        layout.addWidget(QLabel("Fecha de Movimiento:"))
        self.fecha_picker = QDateEdit()
        self.fecha_picker.setCalendarPopup(True)
        layout.addWidget(self.fecha_picker)

        layout.addWidget(QLabel("Fecha de Vencimiento:"))
        self.vencimiento_picker = QDateEdit()
        self.vencimiento_picker.setCalendarPopup(True)
        layout.addWidget(self.vencimiento_picker)

        # Observaciones
        layout.addWidget(QLabel("Observaciones:"))
        self.observaciones_input = QTextEdit()
        layout.addWidget(self.observaciones_input)

        # Botones
        botones = QHBoxLayout()
        self.guardar_btn = QPushButton("Guardar")
        self.limpiar_btn = QPushButton("Limpiar")
        botones.addWidget(self.guardar_btn)
        botones.addWidget(self.limpiar_btn)
        layout.addLayout(botones)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EntradaSalidaTab()
    ventana.show()
    sys.exit(app.exec())