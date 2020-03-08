from PyQt5.QtWidgets import *


class InputURLWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.layout = QHBoxLayout()

        self.label = QLabel()
        self.label.setText('URL: ')
        self.layout.addWidget(self.label)

        self.lineEdit = QLineEdit()
        self.layout.addWidget(self.lineEdit)

        self.setLayout(self.layout)

    def getInput(self):
        return self.lineEdit.text()
