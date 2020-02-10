from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
from PyQt5.QtCore import *


class FileDownloadManager(QObject):
    '''
    FileDownloadManager is for handling file downloads.
    replyHandlers set holds links to valid ReplyHandlers to prevent them from deleting by garbage collector.
    '''
    class ReplyHandler():
        def __init__(self, reply, filename, fileDownloadManager):
            self.reply = reply
            self.filename = filename
            self.fileDownloadManager = fileDownloadManager

        def handleReply(self):
            byteArray = self.reply.readAll()
            file = QFile(self.filename)
            file.open(QIODevice.WriteOnly)
            file.write(byteArray)
            file.close()
            self.fileDownloadManager.replyHandlers.remove(self)

    def __init__(self):
        super(QObject, self).__init__()
        
        self.accessManager = QNetworkAccessManager()
        self.replyHandlers = set()

    def downloadFile(self, url, filename):
        request = QNetworkRequest()
        request.setUrl(QUrl(url))

        reply = self.accessManager.get(request)
        replyHandler = self.ReplyHandler(reply, filename, self)
        reply.finished.connect(replyHandler.handleReply)
        self.replyHandlers.add(replyHandler)

        return reply.downloadProgress


if __name__ == '__main__':
    '''
    Simple example for downloading one file.
    '''
    app = QApplication([])
    window = QMainWindow()
    window.show()

    url = 'https://google.com/index.html'
    filename = 'index.html'
    fd = FileDownloadManager()
    fd.downloadFile(url, filename)

    app.exec_()
