# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/mainwindowL30709.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mastermind import Mastermind
from gameoverdialog import Ui_gameoverDialog
from basemainwindow import Ui_BaseMainWindow

class Ui_MainWindow(Ui_BaseMainWindow):
    def __init__(self):
        super().__init__()

    def game_init(self):
        self.selectedColors = []
        self.tries = 0
        self.mastermind.solution = self.mastermind.get_random_solution()
        del self.mastermind.scores[:]
        del self.mastermind.guesses[:]
        self.update_models()
        self.mastermind.is_over = False

    def setupUi(self, MainWindow, MastermindObj, oldGuessesModel, scoresModel, size = None):
        self.mastermind = MastermindObj
        self.mainwindow = MainWindow
        self.oldGuessesModel = oldGuessesModel
        self.scoresModel = scoresModel
        
        super().setupUi(MainWindow)

        if size is not None:
            self.mainwindow.resize(size)

        self.game_init()
        MainWindow.setObjectName("MainWindow")

        self.resetButton.clicked.connect(self.resetButtonClicked)
        self.colorsTable.cellClicked['int','int'].connect(self.clicked_color)
        self.submitButton.clicked.connect(self.clicked_submit)

    def resetButtonClicked(self):
        self.selectedColors = []
        self.set_thisguesstable()

    def set_thisguesstable(self):
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled)
        self.thisGuessTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled)
        self.thisGuessTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled)
        self.thisGuessTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDropEnabled)
        self.thisGuessTable.setItem(0, 3, item)

    def clicked_color(self, row, col):
        if len(self.selectedColors) >= 4:
            return
        self.selectedColors.append(col)

        item = self.thisGuessTable.item(0, len(self.selectedColors)-1)
        color = self.colorsTable.item(row,col).background().color()
        brush = QtGui.QBrush(color)
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush) 

    def clicked_submit(self):
        if self.mastermind.is_over:
            self.game_restart()
            return
        if len(self.selectedColors) != 4:
            return
        print(self.selectedColors)

        correct, misplaced = self.mastermind.check_guess(self.selectedColors)
        self.update_models()

        self.selectedColors = []
        self.tries += 1
        self.set_thisguesstable()

        if correct == 4:
            self.colorsTable.setEnabled(False)
            self.mastermind.is_over = True
            self.submitButton.setText("Reset")
            self.show_game_over("won")
        elif self.tries == 10:
            self.colorsTable.setEnabled(False)
            self.mastermind.is_over = True
            self.submitButton.setText("Reset")
            self.show_game_over("lost")
            # game lost

    def update_models(self):
        self.oldGuessesModel.dataChanged.emit(self.oldGuessesModel.index(0, 0), self.oldGuessesModel.index(0, self.oldGuessesModel.rowCount(self.oldGuessesModel.index)))
        self.scoresModel.dataChanged.emit(self.scoresModel.index(0, 0), self.scoresModel.index(0, self.scoresModel.rowCount(self.scoresModel.index)))

    def show_game_over(self, text):
        Dialog = QtWidgets.QDialog(self.centralwidget)
        ui = Ui_gameoverDialog(text)
        ui.setupUi(Dialog)
        #Dialog.show()
        choice = Dialog.exec_()

        if choice == QtWidgets.QDialog.Accepted:
            self.game_restart()
            pass
        else:
            pass

    def game_restart(self):
        self.game_init()
        self.colorsTable.setEnabled(True)
        self.submitButton.setText("Submit")
