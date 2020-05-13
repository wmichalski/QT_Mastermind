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

    def game_init(self, MastermindObj):
        self.selectedColors = []
        self.tries = 0
        self.mastermind = MastermindObj
        self.mastermind.get_random_solution()

    def setupUi(self, MainWindow, MastermindObj):
        self.mainwindow = MainWindow
        super().setupUi(MainWindow)
        self.game_init(MastermindObj)
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
        for col in range(4):
            color = self.thisGuessTable.item(0,col).background().color()
            brush = QtGui.QBrush(color)
            brush.setStyle(QtCore.Qt.SolidPattern)
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(brush) 
            self.oldGuessesTable.setItem(self.tries, col, item)

        correct, misplaced = self.mastermind.check_guess(self.selectedColors)
        self.print_score(correct, misplaced)

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
        mastermind = Mastermind()
        self.setupUi(self.mainwindow, mastermind)

    def print_score(self, correct, misplaced):
        for col in range(4):
            if correct:
                correct -= 1
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(brush) 
                self.scoreTable.setItem(self.tries, col, item)
            elif misplaced:
                misplaced -=1
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(brush) 
                self.scoreTable.setItem(self.tries, col, item)

