import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mastermind import Mastermind
from gameoverdialog import Ui_gameoverDialog
from basemainwindow import Ui_BaseMainWindow
from mainwindow import Ui_MainWindow

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        try:
            # if role == QtCore.Qt.DisplayRole:
            #     return self._data[index.row()][index.column()]

            if role == QtCore.Qt.BackgroundRole:
                value = self._data[index.row()][index.column()]
                if value == 0:
                    return QtGui.QColor("#F70D1A")
                if value == 1:
                    return QtGui.QColor("#FF5F00")
                if value == 2:
                    return QtGui.QColor("#FFE302")
                if value == 3:
                    return QtGui.QColor("#A6D608")
                if value == 4:
                    return QtGui.QColor("#00AAEE")
                if value == 5:
                    return QtGui.QColor("#9F00FF")
                if value == 10:
                    return QtGui.QColor(20, 20, 20)
                if value == 11:
                    return QtGui.QColor(230, 230, 230)
        except:
            pass

    def rowCount(self, index):
        return 10

    def columnCount(self, index):
        return 4

if __name__ == "__main__":
    mastermind = Mastermind()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    model_guesses = TableModel(mastermind.guesses)
    model_scores = TableModel(mastermind.scores)

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, mastermind, model_guesses, model_scores)

    ui.oldGuessesView.setModel(model_guesses)
    ui.scoreView.setModel(model_scores)

    for i in range(4):
        ui.oldGuessesView.setColumnWidth(i, 50)

    for i in range(10):
        ui.oldGuessesView.setRowHeight(i, 50)
    
    for i in range(4):
        ui.scoreView.setColumnWidth(i, 15)

    for i in range(10):
        ui.scoreView.setRowHeight(i, 50)

    MainWindow.show()
    sys.exit(app.exec_())