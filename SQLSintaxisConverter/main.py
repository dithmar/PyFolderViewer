import sys
from PyQt5.QtWidgets import QApplication
import ui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ui.MainWindow()
    window.setWindowTitle("Conversor de MySQL a PostgreSQL")
    window.show()
    sys.exit(app.exec_())
