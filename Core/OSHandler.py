import os
import validators


defaultDownloadFolder = os.path.expanduser('~/Downloads')

def checkURL(url):
    return validators.url(url)

def checkFilename(filename):
    return os.path.isabs(filename)

def getDefaultDownloadFolder():
    return defaultDownloadFolder

def openFileWithDefaultApp(filename):
    os.system('xdg-open {}'.format(filename))
