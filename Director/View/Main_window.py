# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.scrollArea = QtWidgets.QScrollArea(MainWindow)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 1280, 720))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(290, 0, 1280, 31))

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(290, 0, 1280, 31))

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1275, 653))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.tableWidget)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 40, 1250, 720))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.ensureVisible(0,0, xMargin=50, yMargin=50)


        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 0, 271, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("История платежей")
        self.comboBox.addItem("Должники")
        self.comboBox.addItem("Инвентарь")
        self.comboBox.addItem("Платежи предприятия")
        self.comboBox.addItem("История регионов")


        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(300, 0, 191, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton1 = QtWidgets.QPushButton(self.widget1)
        self.pushButton1.setGeometry(QtCore.QRect(300, 0, 191, 31))
        self.pushButton1.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QDateEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(500, 0, 191, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QDateEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(720, 0, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit1 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit1.setGeometry(QtCore.QRect(500, 0, 191, 31))
        self.lineEdit1.setObjectName("lineEdit1")

        self.lineEdit1_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit1_2.setGeometry(QtCore.QRect(720, 0, 191, 31))
        self.lineEdit1_2.setObjectName("lineEdit1_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 31))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")

        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")

        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")

        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")

        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")

        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Показать"))
        self.pushButton1.setText(_translate("MainWindow", "Показать"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "Добавить пользователя"))
        self.action_2.setText(_translate("MainWindow", "Добавить обьект"))
        self.action_3.setText(_translate("MainWindow", "Добавить регион"))
        self.action_4.setText(_translate("MainWindow", "Выделить участок"))
        self.action_5.setText(_translate("MainWindow", "Оплата услуг председателя"))
        self.action_6.setText(_translate("MainWindow", "Услуги садоводства"))

