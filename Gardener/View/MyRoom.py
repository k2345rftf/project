# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyRoom.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(573, 418)
        self.buttonBox = QtWidgets.QPushButton(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 370, 190, 32))
        self.buttonBox.setObjectName("buttonBox")
        self.button = QtWidgets.QPushButton(Dialog)
        self.button.setGeometry(QtCore.QRect(250, 370, 300, 32))
        self.button.setObjectName("buttonBox")
        self.ShareTable = QtWidgets.QTableWidget(Dialog)
        self.ShareTable.setGeometry(QtCore.QRect(30, 50, 301, 41))
        self.ShareTable.setObjectName("ShareTable")
        self.ShareTable.setColumnCount(0)
        self.ShareTable.setRowCount(0)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 351, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 231, 17))
        self.label_2.setObjectName("label_2")
        self.CounterUn = QtWidgets.QCommandLinkButton(Dialog)
        self.CounterUn.setGeometry(QtCore.QRect(20, 240, 250, 41))
        self.CounterUn.setObjectName("CounterUn")
        self.ChPass = QtWidgets.QLineEdit(Dialog)
        self.ChPass.setGeometry(QtCore.QRect(30, 140, 241, 27))
        self.ChPass.setObjectName("ChPass")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Личный кабинет"))
        self.label.setText(_translate("Dialog", "Номер региона и занимаемая площадь"))
        self.label_2.setText(_translate("Dialog", "Изменить пароль"))
        self.buttonBox.setText(_translate("Dialog", "Сохранить пароль"))
        self.button.setText(_translate("Dialog", "Выход"))
        self.CounterUn.setText(_translate("Dialog", "Добавить счетчик"))

