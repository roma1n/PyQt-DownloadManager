from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QUrl
from PyQt5.QtGui import QDesktopServices

from Window import Window
from FileDownloadManager import FileDownloadManager


class Application(QApplication):
    '''
    The main class for Download manager.
    '''
    def __init__(self):
        super(QApplication, self).__init__([])

        self.aboutUrl = QUrl('https://google.com')
        self.applicationTitle = 'Download Manager'

        self.fileDownloadManager = FileDownloadManager()
        self.initActions()
        self.initWindow()
        self.exec_()

    def initActions(self):
        self.actionsHolder = QObject()
        self.actionNew = self.buildAction('&New', function=self.downloadFile, shortcut='Ctrl+N')
        self.actionAbout = self.buildAction('&About', function=self.about)

    def initWindow(self):
        self.window = Window()

    def downloadFile(self):
        url, _ = QInputDialog.getText(None, "File URL","URL:", QLineEdit.Normal, "")
        filename, _ = QFileDialog.getSaveFileName(None, 'File Name')
        progress = self.fileDownloadManager.downloadFile(url, filename)
        self.window.workspace.downloadList.addDownload(filename, url, progress)

    def about(self):
        self.openBrowser(self.aboutUrl)

    def openBrowser(self, url):
        QDesktopServices.openUrl(url)

    def buildAction(self, title, function=None, shortcut=None):
        action = QAction(title, self.actionsHolder)
        if function != None:
            action.triggered.connect(function)
        if shortcut != None:
            action.setShortcut(shortcut)
        return action


if __name__ == '__main__':
    app = Application()
