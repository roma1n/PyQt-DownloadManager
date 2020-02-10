from PyQt5.QtWidgets import *


class DownloadWidget(QWidget):
    '''
    Widget shows information about single file to be download.
    Contains filename, url, progress bar.
    '''
    def update(self, val, maxval):
        if maxval != -1:
            self.progressBar.setMaximum(maxval)
            self.progressBar.setValue(val)
            self.progressBar.setMinimum(0)

    def __init__(self, filename, url, progress, parent=None):
        super(QWidget, self).__init__(parent)

        self.filename = filename
        self.url = url

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.filenameLabel = QLabel(self)
        self.filenameLabel.setText('File:{_filename}'.format(_filename=self.filename))
        self.layout.addWidget(self.filenameLabel)

        self.urlLabel = QLabel(self)
        self.urlLabel.setText('URL:{_url}'.format(_url=self.url))
        self.layout.addWidget(self.urlLabel)

        self.progressBar = QProgressBar(self)
        self.progress = progress
        self.progress.connect(self.update)
        self.layout.addWidget(self.progressBar)

        self.show()
