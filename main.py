# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/mainwindowL30709.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mastermind import Mastermind
from gameoverdialog import Ui_gameoverDialog


class Ui_MainWindow(object):

    def setupUi(self, MainWindow, MastermindObj):
        self.selectedColors = []
        self.tries = 0
        self.mastermind = MastermindObj
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(303, 759)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("diamond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(0, 670, 301, 61))
        self.submitButton.setAcceptDrops(False)
        self.submitButton.setObjectName("submitButton")
        self.oldGuessesTable = QtWidgets.QTableWidget(self.centralwidget)
        self.oldGuessesTable.setEnabled(False)
        self.oldGuessesTable.setGeometry(QtCore.QRect(0, 0, 201, 501))
        self.oldGuessesTable.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.oldGuessesTable.setBaseSize(QtCore.QSize(4, 10))
        self.oldGuessesTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.oldGuessesTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.oldGuessesTable.setAutoScroll(False)
        self.oldGuessesTable.setWordWrap(False)
        self.oldGuessesTable.setCornerButtonEnabled(False)
        self.oldGuessesTable.setObjectName("oldGuessesTable")
        self.oldGuessesTable.setColumnCount(4)
        self.oldGuessesTable.setRowCount(10)
        self.oldGuessesTable.horizontalHeader().setVisible(False)
        self.oldGuessesTable.horizontalHeader().setDefaultSectionSize(50)
        self.oldGuessesTable.horizontalHeader().setMinimumSectionSize(0)
        self.oldGuessesTable.verticalHeader().setVisible(False)
        self.oldGuessesTable.verticalHeader().setCascadingSectionResizes(False)
        self.oldGuessesTable.verticalHeader().setDefaultSectionSize(50)
        self.oldGuessesTable.verticalHeader().setMinimumSectionSize(0)
        self.colorsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.colorsTable.setGeometry(QtCore.QRect(0, 600, 301, 51))
        self.colorsTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.colorsTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.colorsTable.setRowCount(1)
        self.colorsTable.setColumnCount(6)
        self.colorsTable.setObjectName("colorsTable")
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.colorsTable.setItem(0, 5, item)
        self.colorsTable.horizontalHeader().setVisible(False)
        self.colorsTable.horizontalHeader().setDefaultSectionSize(50)
        self.colorsTable.verticalHeader().setVisible(False)
        self.colorsTable.verticalHeader().setDefaultSectionSize(50)
        self.thisGuessTable = QtWidgets.QTableWidget(self.centralwidget)
        self.thisGuessTable.setGeometry(QtCore.QRect(0, 530, 201, 51))
        self.thisGuessTable.setAcceptDrops(True)
        self.thisGuessTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.thisGuessTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.thisGuessTable.setRowCount(1)
        self.thisGuessTable.setColumnCount(4)
        self.thisGuessTable.setObjectName("thisGuessTable")
        self.set_thisguesstable()
        self.thisGuessTable.horizontalHeader().setVisible(False)
        self.thisGuessTable.horizontalHeader().setDefaultSectionSize(50)
        self.thisGuessTable.verticalHeader().setVisible(False)
        self.thisGuessTable.verticalHeader().setDefaultSectionSize(50)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.scoreTable = QtWidgets.QTableWidget(self.centralwidget)
        self.scoreTable.setEnabled(False)
        self.scoreTable.setGeometry(QtCore.QRect(220, 0, 61, 501))
        self.scoreTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scoreTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scoreTable.setWordWrap(False)
        self.scoreTable.setCornerButtonEnabled(False)
        self.scoreTable.setRowCount(10)
        self.scoreTable.setColumnCount(4)
        self.scoreTable.setObjectName("scoreTable")
        self.scoreTable.horizontalHeader().setVisible(False)
        self.scoreTable.horizontalHeader().setDefaultSectionSize(15)
        self.scoreTable.verticalHeader().setVisible(False)
        self.scoreTable.verticalHeader().setDefaultSectionSize(50)

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(220, 530, 51, 51))
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.resetButtonClicked)

        self.retranslateUi(MainWindow)
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
            self.show_game_over("won")
        elif self.tries == 10:
            self.colorsTable.setEnabled(False)
            self.show_game_over("lost")
            # game lost

    def show_game_over(self, text):
        Dialog = QtWidgets.QDialog(self.centralwidget)
        ui = Ui_gameoverDialog(text)
        ui.setupUi(Dialog)
        #Dialog.show()
        choice = Dialog.exec_()

        if choice == QtWidgets.QDialog.Accepted:
            self.setupUi(MainWindow, mastermind)
            pass
        else:
            pass

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
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mastermind"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        __sortingEnabled = self.colorsTable.isSortingEnabled()
        self.colorsTable.setSortingEnabled(False)
        self.colorsTable.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.thisGuessTable.isSortingEnabled()
        self.thisGuessTable.setSortingEnabled(False)
        self.thisGuessTable.setSortingEnabled(__sortingEnabled)
        self.resetButton.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    mastermind = Mastermind()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, mastermind)
    MainWindow.show()
    sys.exit(app.exec_())


