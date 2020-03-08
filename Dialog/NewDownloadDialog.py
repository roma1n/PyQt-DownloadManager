from PyQt5.QtWidgets import *

from Dialog.NewDownloadWidget import NewDownloadWidget


class NewDownloadDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setWindowTitle("New File Download")

        self.layout = QVBoxLayout(self)
        self.newDownloadWidget = NewDownloadWidget()
        self.layout.addWidget(self.newDownloadWidget)
        self.newDownloadWidget.show()

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.addButton(QDialogButtonBox.Ok)
        self.buttonBox.addButton(QDialogButtonBox.Cancel)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)

    def getInput(self):
        return self.newDownloadWidget.getInput()
