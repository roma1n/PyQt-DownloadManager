from PyQt5.QtWidgets import *

import Core.OSHandler as OSHandler


class InputFilenameWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.layout = QHBoxLayout()

        self.label = QLabel()
        self.label.setText('File: ')
        self.layout.addWidget(self.label)

        self.lineEdit = QLineEdit()
        self.layout.addWidget(self.lineEdit)

        self.browseButton = QPushButton()
        self.browseButton.setText('Browse')
        self.browseButton.clicked.connect(self.updateFilename)
        self.layout.addWidget(self.browseButton)

        self.setLayout(self.layout)

    def getInput(self):
        return self.lineEdit.text()

    def updateFilename(self):
        options = QFileDialog.Options()
        newFilename, _ = QFileDialog.getSaveFileName(None, 'File Name', 
            directory=OSHandler.getDefaultDownloadFolder(), 
            options=options)
        self.lineEdit.setText(newFilename)
