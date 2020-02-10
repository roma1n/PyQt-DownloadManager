from PyQt5.QtWidgets import *

from DownloadListWidget import DownloadListWidget


class Workspace(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.downloadList = DownloadListWidget(self)
        self.scrollDownloadList = QScrollArea()
        self.scrollDownloadList.setWidget(self.downloadList)
        self.scrollDownloadList.setWidgetResizable(True)
        self.downloadList.show()

        self.layout.addWidget(self.scrollDownloadList)

        self.show()
