import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLabel, QWidget
from PyQt5.uic import loadUi
from main_ui import Ui_MainWindow
import database
import time


class Window(QMainWindow, Ui_MainWindow):

	def __init__(self, parent=None):

		super().__init__(parent)

		self.setupUi(self)
		self.setGeometry(100, 100, 800, 480)
		self.UiComponents()
		self.show()

	def UiComponents(self):
		self.showMaximized()

        

if __name__ == "__main__":

    while True:
        app = QApplication(sys.argv)
        win = Window()
        win.show()
        x = database.get_current_tag()
        win.label.setText(x)
        QWidget.update()
        sys.exit(app.exec())
