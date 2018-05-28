# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MW.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TableView = QtWidgets.QTableWidget(MainWindow)
        self.TableView.setGeometry(QtCore.QRect(0, 65, 1280, 720))
        self.TableView.setObjectName("TableView")
        self.TableView.setColumnCount(0)
        self.TableView.setRowCount(0)
        self.dateEdit = QtWidgets.QDateEdit(MainWindow)
        self.dateEdit.setGeometry(QtCore.QRect(10, 30, 110, 25))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit1 = QtWidgets.QDateEdit(MainWindow)
        self.dateEdit1.setGeometry(QtCore.QRect(150, 30, 110, 25))
        self.dateEdit1.setObjectName("dateEdit1")
        self.enter = QtWidgets.QPushButton(MainWindow)
        self.enter.setGeometry(QtCore.QRect(300, 30, 99, 30))
        self.enter.setObjectName("enter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        # self.choose.setItemText(0, _translate("MainWindow", "Регионы во владении"))
        # self.choose.setItemText(1, _translate("MainWindow", "История платежей"))
        self.action_2.setText(_translate("MainWindow", "Личный Кабинет"))
        self.action_3.setText(_translate("MainWindow", "Внести показания счетчика"))
        self.enter.setText(_translate("MainWindow", "Показать"))

