import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from ui import MainWindow
import logic

def import_json():
    window.import_json()

def generate_sql():
    json_file_path = window.get_json_file_path()
    database = window.get_selected_database()

    if not json_file_path:
        QMessageBox.warning(window, "Error", "No se ha seleccionado un archivo JSON.")
        return

    sql_code, nombre_archivo = logic.import_json(json_file_path, database)

    if sql_code is not None and nombre_archivo is not None:
        try:
            with open(nombre_archivo, "w") as sql_file:
                sql_file.write(sql_code)
            QMessageBox.information(window, "Generación de código en SQL completada",
                                    f"El código generado se ha guardado en: {nombre_archivo}")
        except Exception as e:
            QMessageBox.warning(window, "Error", f"Error al guardar el archivo SQL: {str(e)}")
    else:
        QMessageBox.warning(window, "Error", "No se pudo generar el código SQL.")

app = QApplication(sys.argv)

window = MainWindow()
window.import_button.clicked.connect(import_json)
window.generate_button.clicked.connect(generate_sql)

window.show()

sys.exit(app.exec_())
