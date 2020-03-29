from PyQt5.QtWidgets import *

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super(QMenuBar, self).__init__(parent)

        qApp = QApplication.instance()

        self.fileMenu = self.addMenu('&File')
        self.fileMenu.addAction(qApp.actionNew)
        self.fileMenu.addAction(qApp.actionYoutube)
        
        self.aboutMenu = self.addMenu('&About')
        self.aboutMenu.addAction(qApp.actionAbout)
