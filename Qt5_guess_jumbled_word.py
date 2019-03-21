from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Randomizer - Game"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


App = QApplication(sys.argv)
game = Window()
sys.exit(App.exec())
