from PyQt5.QtWidgets import *

from Workspace import Workspace
from MenuBar import MenuBar


class Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.setWindowTitle(QApplication.instance().applicationTitle)

        self.setFixedSize(800, 600)
        self.initUI()
        self.show()

    def initUI(self):
        self.menuBar = MenuBar(self)
        self.setMenuBar(self.menuBar)
        self.workspace = Workspace(self)
        self.setCentralWidget(self.workspace)
