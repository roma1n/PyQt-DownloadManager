from PyQt5.QtWidgets import *

from Dialog.NewDownloadWidget import NewDownloadWidget
import Dialog.WarningMessage as WarningMessage
import Core.OSHandler as OSHandler


class NewDownloadDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setWindowTitle("New File Download")

        self.layout = QVBoxLayout(self)
        self.newDownloadWidget = NewDownloadWidget()
        self.layout.addWidget(self.newDownloadWidget)
        self.newDownloadWidget.show()

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.accepted.connect(self.acceptDownload)
        self.buttonBox.rejected.connect(self.rejectDownload)
        self.buttonBox.addButton(QDialogButtonBox.Ok)
        self.buttonBox.addButton(QDialogButtonBox.Cancel)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)

    def acceptDownload(self):
        url, filename = self.getInput()
        if not OSHandler.checkURL(url):
            WarningMessage.showWarningMessage(parent=self, text='Bad URL!')
            return
        if not OSHandler.checkFilename(filename):
            return
        self.accept()

    def rejectDownload(self):
        self.reject()

    def getInput(self):
        return self.newDownloadWidget.getInput()
