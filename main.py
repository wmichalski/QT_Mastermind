import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mastermind import Mastermind
from gameoverdialog import Ui_gameoverDialog
from basemainwindow import Ui_BaseMainWindow
from mainwindow import Ui_MainWindow

if __name__ == "__main__":
    mastermind = Mastermind()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, mastermind)
    MainWindow.show()
    sys.exit(app.exec_())


