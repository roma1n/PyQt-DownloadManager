from PyQt5.QtWidgets import *

from Dialog.InputFilenameWidget import InputFilenameWidget
from Dialog.InputURLWidget import InputURLWidget


class NewDownloadWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.layout = QVBoxLayout()

        self.inputURLWidget = InputURLWidget(self)
        self.layout.addWidget(self.inputURLWidget)

        self.inputFilenameWidget = InputFilenameWidget(self)
        self.layout.addWidget(self.inputFilenameWidget)

        self.setLayout(self.layout)

    def getInput(self):
        url = self.inputURLWidget.getInput()
        filename = self.inputFilenameWidget.getInput()
        return url, filename
