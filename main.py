import sys
import random

from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from game_ui import Ui_MainWindow

database = ["The Walking Dead", "The Big Bang Theory", "Sherlock", "Game of Thrones", "Twilight", "Person of Interest",
            "How I Met Your Mother", "Friends", "Black Mirror", "Arrow", "The Flash", "Suits", "Riverdale", "The Office",
            "Lost", "Thirteen Reasons Why", "Breaking Bad", "How to get away with Murder", "Modern Family", "Endeavour",
            "Westworld", "Prison Break", "Orange is the new Black", "Mindhunter", "Altered Carbon", "Daredevil",
            "Da Vincis Demons", "House of Cards", "Young Sheldon", "Castle"]

chosen = []

# https://gist.github.com/dbspringer/1268192/2c334f48e40a8c57acc34e399820980445efbb0c
def scramble(unscrambled):
    import string, random, re
    splitter = re.compile(r'\s')
    words = splitter.split(u''.join(ch for ch in unscrambled if ch not in set(string.punctuation)))
    for word in words:
        mid = list(word[0:])
        random.shuffle(mid)
        scrambled = ''.join(mid)
        unscrambled = unscrambled.replace(word, scrambled, 1)

    return unscrambled

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Randomizery")
        self.setupUi(self)
        self.restart()

    def clear(self):
        _translate = QtCore.QCoreApplication.translate
        for i in range(10):
            eval(f"self.ans{i}.setText(_translate(\"MainWindow\", \"\"))")
            eval(f"self.c{i}.setChecked(False)")
        self.points.display(0)
        print("Cleared Answer Fields")

    def submit(self):
        _translate = QtCore.QCoreApplication.translate
        score = 0
        for i in range(10):
            answer = eval(f"self.ans{i}.text()")
            if answer.lower() == database[i].lower():
                score = score + 1
                eval(f"self.c{i}.setChecked(True)")
        self.points.display(score)
        print("Checked and Updated")

    def restart(self):
        _translate = QtCore.QCoreApplication.translate
        random.shuffle(database)
        for i in range(10):
            eval(f"self.game{i}.setText(_translate(\"MainWindow\", \"{ scramble(database[i].lower()) }\"))")
        self.clear()

        print("Game Initialized... ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Window()
    game.show()
    sys.exit(app.exec_())
