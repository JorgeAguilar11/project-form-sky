from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit,
    QComboBox, QDateEdit, QCheckBox, QTextEdit, QPushButton, QMessageBox, QScrollArea
)
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtCore import QDate
import sys

class FormularioEntrada(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario de Entrada de Mercancía")
        self.setMinimumWidth(700)
        layout = QVBoxLayout()

        # --- Información General del Producto ---
        grupo_producto = QGroupBox("INFORMACIÓN GENERAL DEL PRODUCTO")
        grupo_producto.setStyleSheet("QGroupBox { font-weight: bold; color: white; font-size: 14pt; background-color: #444; }")
        layout_producto = QVBoxLayout()

        # Nombre del producto
        label_nombre = QLabel("Nombre del producto:")
        label_nombre.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.nombre_input = QLineEdit()
        self.nombre_input.setMinimumWidth(400)
        layout_producto.addWidget(label_nombre)
        layout_producto.addWidget(self.nombre_input)

        # Código del producto
        label_codigo = QLabel("Código del producto:")
        label_codigo.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.codigo_input = QLineEdit()
        self.codigo_input.setValidator(QIntValidator())
        self.codigo_input.setFixedWidth(120)
        layout_producto.addWidget(label_codigo)
        layout_producto.addWidget(self.codigo_input)

        # Proveedor
        label_proveedor = QLabel("Proveedor:")
        label_proveedor.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.proveedor_combo = QComboBox()
        self.proveedor_combo.addItems([
            "NEGOCIOS CENTROAMERICANOS, S.A.", "PROVEEDOR 2", "PROVEEDOR 3"
        ])
        layout_producto.addWidget(label_proveedor)
        layout_producto.addWidget(self.proveedor_combo)

        # Cantidad y Unidad en la misma línea
        cantidad_layout = QHBoxLayout()
        cantidad_label = QLabel("CANTIDAD:")
        cantidad_label.setStyleSheet("color: white; font-weight: bold;")
        self.cantidad_input = QLineEdit()
        self.cantidad_input.setValidator(QIntValidator())
        self.cantidad_input.setFixedWidth(80)
        unidad_label = QLabel("Unidad de medida:")
        unidad_label.setStyleSheet("color: #CCCCCC; font-size: 10pt; margin-left: 10px;")
        self.unidad_combo = QComboBox()
        self.unidad_combo.addItems(["C/U", "LB", "KG"])
        self.unidad_combo.setFixedWidth(80)
        cantidad_layout.addWidget(cantidad_label)
        cantidad_layout.addWidget(self.cantidad_input)
        cantidad_layout.addSpacing(10)
        cantidad_layout.addWidget(unidad_label)
        cantidad_layout.addWidget(self.unidad_combo)
        cantidad_layout.addStretch()
        layout_producto.addLayout(cantidad_layout)

        grupo_producto.setLayout(layout_producto)

        # --- Información del Lote y Recepción ---
        grupo_lote = QGroupBox("INFORMACIÓN DEL LOTE Y RECEPCIÓN")
        grupo_lote.setStyleSheet("QGroupBox { font-weight: bold; color: white; font-size: 14pt; background-color: #444; }")
        layout_lote = QVBoxLayout()
        label_lote = QLabel("Lote/Datum:")
        label_lote.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.lote_input = QLineEdit()
        self.lote_input.setFixedWidth(150)
        layout_lote.addWidget(label_lote)
        layout_lote.addWidget(self.lote_input)

        label_fecha = QLabel("Fecha de recepción:")
        label_fecha.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.fecha_recepcion = QDateEdit()
        self.fecha_recepcion.setCalendarPopup(True)
        self.fecha_recepcion.setDisplayFormat("dd/MMM/yy")
        self.fecha_recepcion.setDate(QDate.currentDate())
        layout_lote.addWidget(label_fecha)
        layout_lote.addWidget(self.fecha_recepcion)

        label_tipo = QLabel("Tipo de producto:")
        label_tipo.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.tipo_producto_combo = QComboBox()
        self.tipo_producto_combo.addItems(["N_TA", "F_Ref", "C_Cong"])
        layout_lote.addWidget(label_tipo)
        layout_lote.addWidget(self.tipo_producto_combo)

        grupo_lote.setLayout(layout_lote)

        # --- Inspección y Cumplimiento ---
        grupo_inspeccion = QGroupBox("INSPECCIÓN Y CUMPLIMIENTO")
        grupo_inspeccion.setStyleSheet("QGroupBox { font-weight: bold; color: white; font-size: 14pt; background-color: #444; }")
        layout_inspeccion = QVBoxLayout()
        label_estado = QLabel("Estado del producto:")
        label_estado.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.estado_combo = QComboBox()
        self.estado_combo.addItems(["Ok", "Rechazado"])
        layout_inspeccion.addWidget(label_estado)
        layout_inspeccion.addWidget(self.estado_combo)

        self.cumple_politica = QCheckBox("Cumple política de recepción")
        self.cumple_politica.setStyleSheet("color: #CCCCCC;")
        layout_inspeccion.addWidget(self.cumple_politica)

        self.estado_congelado = QCheckBox("Estado sólido congelado")
        self.estado_congelado.setStyleSheet("color: #CCCCCC;")
        layout_inspeccion.addWidget(self.estado_congelado)

        self.cumple_temp = QCheckBox("Cumple con temperatura requerida")
        self.cumple_temp.setStyleSheet("color: #CCCCCC;")
        layout_inspeccion.addWidget(self.cumple_temp)

        temp_layout = QHBoxLayout()
        temp_label = QLabel("Temperatura registrada:")
        temp_label.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.temperatura_input = QLineEdit()
        self.temperatura_input.setValidator(QDoubleValidator(-100, 100, 2))
        self.temperatura_input.setFixedWidth(80)
        self.temp_unidad_combo = QComboBox()
        self.temp_unidad_combo.addItems(["°C", "Temp. Amb"])
        self.temp_unidad_combo.setFixedWidth(100)
        temp_layout.addWidget(temp_label)
        temp_layout.addWidget(self.temperatura_input)
        temp_layout.addWidget(self.temp_unidad_combo)
        layout_inspeccion.addLayout(temp_layout)

        grupo_inspeccion.setLayout(layout_inspeccion)

        # --- Observaciones y Seguimiento ---
        grupo_obs = QGroupBox("OBSERVACIONES Y SEGUIMIENTO")
        grupo_obs.setStyleSheet("QGroupBox { font-weight: bold; color: white; font-size: 14pt; background-color: #444; }")
        layout_obs = QVBoxLayout()
        label_resp = QLabel("Responsable de la recepción:")
        label_resp.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.responsable_combo = QComboBox()
        self.responsable_combo.addItems(["Ariel S", "Basilio DG", "Otro"])
        layout_obs.addWidget(label_resp)
        layout_obs.addWidget(self.responsable_combo)

        label_queja = QLabel("Queja al proveedor:")
        label_queja.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.queja_combo = QComboBox()
        self.queja_combo.addItems(["", "SSCE-SDO", "Proveedor 2"])
        layout_obs.addWidget(label_queja)
        layout_obs.addWidget(self.queja_combo)

        label_queja_det = QLabel("Detalle de queja:")
        label_queja_det.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.queja_detalle = QLineEdit()
        self.queja_detalle.setMinimumWidth(300)
        layout_obs.addWidget(label_queja_det)
        layout_obs.addWidget(self.queja_detalle)

        label_notas = QLabel("Notas adicionales:")
        label_notas.setStyleSheet("color: #CCCCCC; font-size: 10pt;")
        self.notas_input = QTextEdit()
        self.notas_input.setMaximumHeight(60)
        layout_obs.addWidget(label_notas)
        layout_obs.addWidget(self.notas_input)

        grupo_obs.setLayout(layout_obs)

        # --- Botones ---
        botones = QHBoxLayout()
        self.guardar_btn = QPushButton("Guardar")
        self.limpiar_btn = QPushButton("Limpiar")
        botones.addWidget(self.guardar_btn)
        botones.addWidget(self.limpiar_btn)

        # --- Agregar todo al layout principal ---
        layout.addWidget(grupo_producto)
        layout.addWidget(grupo_lote)
        layout.addWidget(grupo_inspeccion)
        layout.addWidget(grupo_obs)
        layout.addLayout(botones)

        # --- Scroll para adaptabilidad ---
        contenedor = QWidget()
        contenedor.setLayout(layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(contenedor)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

        # Conectar botones
        self.guardar_btn.clicked.connect(self.guardar_datos)
        self.limpiar_btn.clicked.connect(self.limpiar_campos)

    def guardar_datos(self):
        # Aquí puedes agregar validaciones y lógica para guardar en CSV o base de datos
        QMessageBox.information(self, "Guardado", "¡Registro guardado (simulado)!")

    def limpiar_campos(self):
        self.nombre_input.clear()
        self.codigo_input.clear()
        self.proveedor_combo.setCurrentIndex(0)
        self.cantidad_input.clear()
        self.unidad_combo.setCurrentIndex(0)
        self.lote_input.clear()
        self.fecha_recepcion.setDate(QDate.currentDate())
        self.tipo_producto_combo.setCurrentIndex(0)
        self.estado_combo.setCurrentIndex(0)
        self.cumple_politica.setChecked(False)
        self.estado_congelado.setChecked(False)
        self.cumple_temp.setChecked(False)
        self.temperatura_input.clear()
        self.temp_unidad_combo.setCurrentIndex(0)
        self.responsable_combo.setCurrentIndex(0)
        self.queja_combo.setCurrentIndex(0)
        self.queja_detalle.clear()
        self.notas_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FormularioEntrada()
    ventana.show()
    sys.exit(app.exec())