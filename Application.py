from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QUrl
from PyQt5.QtGui import QDesktopServices

from Window import Window
from FileDownloadManager import FileDownloadManager
from Dialog.NewDownloadDialog import NewDownloadDialog
from Core.YoutubeDownloader import YoutubeDownloader


class Application(QApplication):
    '''
    The main class for Download manager.
    '''
    def __init__(self):
        super(QApplication, self).__init__([])

        self.aboutUrl = QUrl('https://google.com')
        self.applicationTitle = 'Download Manager'

        self.fileDownloadManager = FileDownloadManager()
        self.youtubeDownloader = YoutubeDownloader()

        self.initActions()
        self.initWindow()
        self.exec_()

    def initActions(self):
        self.actionsHolder = QObject()
        self.actionNew = self.buildAction('&New', function=self.downloadFile, shortcut='Ctrl+N')
        self.actionYoutube = self.buildAction('&Youtube', function=self.downloadVideo, shortcut='Ctrl+Y')
        self.actionAbout = self.buildAction('&About', function=self.about)

    def initWindow(self):
        self.window = Window()

    def downloadFile(self):
        newDownloadDialog = NewDownloadDialog()
        response = newDownloadDialog.exec()
        if response == QDialog.Accepted:
            url, filename = newDownloadDialog.getInput()
            progress = self.fileDownloadManager.downloadFile(url, filename)
            self.window.workspace.downloadList.addDownload(filename, url, progress)

    def downloadVideo(self):
        newDownloadDialog = NewDownloadDialog()
        response = newDownloadDialog.exec()
        if response == QDialog.Accepted:
            url, filename = newDownloadDialog.getInput()
            progress = self.youtubeDownloader.download(url, filename)
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
