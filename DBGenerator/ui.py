from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QComboBox
from PyQt5 import QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generador de código SQL")
        self.resize(300, 180)

        layout = QVBoxLayout()

        self.json_input = QLineEdit()
        self.json_input.setReadOnly(True)
        layout.addWidget(QLabel("Dirección del archivo JSON:"))
        layout.addWidget(self.json_input)

        self.import_button = QPushButton("Importar JSON")
        self.import_button.setStyleSheet(
            """
            QPushButton {
                background-color: #007BFF;
                color: white;
                border: 1px solid #007BFF;
                border-radius: 4px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #0056b3;
                border: 1px solid #0056b3;
            }
            """
        )
        layout.addWidget(self.import_button)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["MySQL", "TransactSQL", "PostgreSQL"])
        layout.addWidget(QLabel("Tipo de base de datos:"))
        layout.addWidget(self.combo_box)

        self.generate_button = QPushButton("Generar código SQL")
        self.generate_button.setStyleSheet(
            """
            QPushButton {
                background-color: #28A745;
                color: white;
                border: 1px solid #28A745;
                border-radius: 4px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #1e7d34;
                border: 1px solid #1e7d34;
            }
            """
        )
        layout.addWidget(self.generate_button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.generate_button.clicked.connect(self.get_data)

    def import_json(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar archivo JSON", "", "Archivos JSON (*.json)")
        if file_path:
            self.json_input.setText(file_path)

    def get_json_file_path(self):
        return self.json_input.text()

    def get_selected_database(self):
        return self.combo_box.currentText()

    def get_data(self):
        pass
