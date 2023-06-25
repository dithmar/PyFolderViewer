import sys
from PyQt5.QtWidgets import QApplication
from ui import MainWindow
import logic

def import_json():
    window.import_json()

def generate_sql():
    json_file_path = window.get_json_file_path()
    logic.import_json(json_file_path)
    data = window.get_data()  # Obtener los datos necesarios para generar el código SQL
    sql_code = logic.generate_sql_code(data)  # Pasar los datos a la función
    # Resto del código para guardar el archivo SQL

app = QApplication(sys.argv)

window = MainWindow()
window.import_button.clicked.connect(import_json)
window.generate_button.clicked.connect(generate_sql)

window.show()

sys.exit(app.exec_())
