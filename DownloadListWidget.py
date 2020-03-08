from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from DownloadWidget import DownloadWidget


class DownloadListWidget(QWidget):
    '''
    Table of downloads.
    Initialized empty, supports adding downloads to the top of the list.
    '''
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

        # set up download table
        self.downloadTable = QTableWidget(0, 3, self)
        self.downloadTableHeaderView = QHeaderView(Qt.Horizontal, self.downloadTable)
        self.downloadTable.setHorizontalHeader(self.downloadTableHeaderView)
        self.downloadTableHeaderView.setSectionResizeMode(QHeaderView.Stretch)
        self.downloadTable.setHorizontalHeaderLabels(['File', 'URL', 'Progress'])
        self.layout.addWidget(self.downloadTable)

    def addDownload(self, filename, url, progress):

        downloadWidget = DownloadWidget(filename, url, progress, self)
        index = self.downloadTable.rowCount()
        self.downloadTable.insertRow(index)
        self.downloadTable.setItem(index, 0, QTableWidgetItem(filename))
        self.downloadTable.setItem(index, 1, QTableWidgetItem(url))
        self.downloadTable.setCellWidget(index, 2, downloadWidget.progressBar)
