from PyQt5.QtWidgets import *

from DownloadListWidget import DownloadListWidget


class Workspace(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.downloadList = DownloadListWidget(self)
        self.layout.addWidget(self.downloadList)
        self.downloadList.show()

        self.show()
