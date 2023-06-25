import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow
from folder_structure import guardar_estructura_carpeta_en_json, guardar_estructura_carpeta_en_txt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Crear la instancia de la interfaz gráfica generada
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar los botones a los métodos correspondientes
        self.ui.btnSeleccionarCarpeta.clicked.connect(self.seleccionar_carpeta)
        self.ui.btnGenerarEstructura.clicked.connect(self.generar_estructura)

    def seleccionar_carpeta(self):
        carpeta = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta de origen")
        self.ui.lineEditCarpeta.setText(carpeta)

    def generar_estructura(self):
        carpeta = self.ui.lineEditCarpeta.text()
        nombre_carpeta = os.path.basename(carpeta)
        ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
        formato_seleccionado = self.ui.comboBoxTipoSalida.currentText()

        if formato_seleccionado == ".json":
            nombre_archivo = os.path.join(ruta_proyecto, nombre_carpeta + "_estructura.json")
            guardar_estructura_carpeta_en_json(carpeta, nombre_archivo)
        elif formato_seleccionado == ".txt":
            nombre_archivo = os.path.join(ruta_proyecto, nombre_carpeta + "_estructura.txt")
            guardar_estructura_carpeta_en_txt(carpeta, nombre_archivo)

        self.ui.statusbar.showMessage("Estructura generada y guardada correctamente.", 3000)
