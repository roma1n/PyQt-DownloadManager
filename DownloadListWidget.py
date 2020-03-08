from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from DownloadWidget import DownloadWidget
import Core.OSHandler as OSHandler


class DownloadListWidget(QWidget):
    '''
    Table of downloads.
    Initialized empty, supports adding downloads.
    '''
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

        # set up download table
        self.downloadTable = QTableWidget(0, 4, self)
        self.downloadTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.downloadTableHeaderView = QHeaderView(Qt.Horizontal, self.downloadTable)
        self.downloadTable.setHorizontalHeader(self.downloadTableHeaderView)
        self.downloadTableHeaderView.setSectionResizeMode(QHeaderView.Stretch)
        self.downloadTable.setHorizontalHeaderLabels(['Path', 'File', 'URL', 'Progress'])
        self.downloadTable.setColumnHidden(0, True)
        self.downloadTable.cellDoubleClicked.connect(self.openFile)
        self.downloadTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.layout.addWidget(self.downloadTable)

    def openFile(self, row, column):
        filename = str(self.downloadTable.item(row, 0).text())
        OSHandler.openFileWithDefaultApp(filename)

    def addDownload(self, filename, url, progress):
        downloadWidget = DownloadWidget(filename, url, progress, self)
        index = self.downloadTable.rowCount()
        self.downloadTable.insertRow(index)
        fileInfo = QFileInfo(filename)
        filenameToShow = fileInfo.fileName()
        self.downloadTable.setItem(index, 0, QTableWidgetItem(filename))
        self.downloadTable.setItem(index, 1, QTableWidgetItem(filenameToShow))
        self.downloadTable.setItem(index, 2, QTableWidgetItem(url))
        self.downloadTable.setCellWidget(index, 3, downloadWidget.progressBar)
