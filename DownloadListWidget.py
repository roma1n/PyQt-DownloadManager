from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from DownloadWidget import DownloadWidget


class DownloadListWidget(QWidget):
    '''
    Shows list of DownloadWidgets. 
    Initialized empty, supports adding DownloadWidgets to the top of the list.
    '''
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

        self.show()

    def addDownload(self, filename, url, progress):
        newDownloadWidget = DownloadWidget(filename, url, progress, self)
        index = self.layout.count() - 1
        self.layout.insertWidget(index, newDownloadWidget)

        self.show()
