from PyQt5.QtWidgets import *

def showWarningMessage(parent=None, title='Warning', text='Something went wrong'):
    dialog = QMessageBox()
    dialog.setWindowTitle(title)
    dialog.setText(text)
    dialog.exec()
