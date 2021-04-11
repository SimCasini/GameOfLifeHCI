import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtWidgets
from GolWindow import GolWindow


class GameApp(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.window = GolWindow()  # la GUI e view controller
        self.window.setWindowTitle('Game of Life')
        self.window.show()
        self.exec_()

if __name__ == "__main__":
    app = GameApp([])
