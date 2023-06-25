from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QVBoxLayout, QWidget, QPushButton, QLineEdit
from pathlib import Path
import sys
import scriptlogic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.selected_file = None

    def init_ui(self):
        self.setWindowTitle("Conversor de MySQL a PostgreSQL")

        # Crear un campo de texto desactivado para mostrar la ruta del archivo seleccionado
        self.file_path_text = QLineEdit()
        self.file_path_text.setReadOnly(True)

        # Crear un botón para abrir el diálogo de selección de archivo
        open_file_button = QPushButton("Abrir archivo")
        open_file_button.clicked.connect(self.open_file_dialog)

        # Crear un botón para realizar la conversión
        convert_button = QPushButton("Convertir")
        convert_button.clicked.connect(self.convert_to_postgresql)

        # Agregar los elementos al diseño de la ventana
        layout = QVBoxLayout()
        layout.addWidget(self.file_path_text)
        layout.addWidget(open_file_button)
        layout.addWidget(convert_button)

        # Crear un widget contenedor y establecer el diseño
        widget = QWidget()
        widget.setLayout(layout)

        # Establecer el widget como el contenido central de la ventana
        self.setCentralWidget(widget)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo SQL", "", "Archivos SQL (*.sql)",
                                                   options=options)

        if file_path:
            self.selected_file = file_path
            self.file_path_text.setText(self.selected_file)

    def convert_to_postgresql(self):
        if self.selected_file:
            input_file = Path(self.selected_file)

            # Leer el contenido del archivo
            with input_file.open("r") as file:
                mysql_sql = file.read()

            # Convertir el código SQL
            postgresql_sql = scriptlogic.convert_to_postgresql(mysql_sql)

            # Obtener la ruta del proyecto
            project_path = Path(__file__).resolve().parent

            # Guardar el código convertido en un nuevo archivo en la raíz del proyecto
            output_file = project_path / f"{input_file.stem}.postgresql.sql"
            with open(output_file, "w") as file:
                file.write(postgresql_sql)

            QMessageBox.information(self, "Conversión completada",
                                    f"La conversión de MySQL a PostgreSQL se ha completado.\n"
                                    f"El código convertido se ha guardado en:\n{output_file}")
        else:
            QMessageBox.warning(self, "Archivo no seleccionado",
                                "No se ha seleccionado ningún archivo.")