import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLabel
from PyQt5.uic import loadUi
from main_ui import Ui_MainWindow


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

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    x = "Hello, World!"
    win.label.setText(x)

    sys.exit(app.exec())
