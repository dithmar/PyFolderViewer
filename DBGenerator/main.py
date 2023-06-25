import sys
from PyQt5.QtWidgets import QApplication
from ui import MainWindow
import logic

def import_json():
    window.import_json()

def generate_sql():
    json_file_path = window.get_json_file_path()
    database = window.get_selected_database()
    logic.import_json(json_file_path, database)  # Pasar el argumento "database"
    data = window.get_data()  # Obtener los datos necesarios para generar el código SQL
    sql_code = logic.generate_sql_code(data, database)  # Pasar los datos y el tipo de base de datos a la función
    # Resto del código para guardar el archivo SQL

app = QApplication(sys.argv)

window = MainWindow()
window.import_button.clicked.connect(import_json)
window.generate_button.clicked.connect(generate_sql)

window.show()

sys.exit(app.exec_())
