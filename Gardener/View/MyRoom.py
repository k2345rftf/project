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
        Dialog.resize(720, 430)
        Dialog.setMinimumSize(QtCore.QSize(720, 430))
        Dialog.setMaximumSize(QtCore.QSize(720, 430))
        
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(300, 50, 350, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.button = QtWidgets.QPushButton(Dialog)
        self.button.setGeometry(QtCore.QRect(30, 370, 150, 32))
        self.button.setObjectName("button")

        self.buttonBox = QtWidgets.QPushButton(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 370, 341, 32))
        self.buttonBox.setObjectName("buttonBox")

        self.TableView = QtWidgets.QTableWidget(Dialog)
        self.TableView.setGeometry(QtCore.QRect(300, 50, 350, 300))
        self.TableView.setObjectName("TableView")
        self.TableView.setColumnCount(0)
        self.TableView.setRowCount(0)

        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.TableView)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(300, 50, 350, 300))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.ensureVisible(0,0, xMargin=50, yMargin=50)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 20, 351, 17))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 231, 17))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 231, 17))
        self.label_3.setObjectName("label_3")

        self.CounterUn = QtWidgets.QCommandLinkButton(Dialog)
        self.CounterUn.setGeometry(QtCore.QRect(20, 240, 230, 41))
        self.CounterUn.setObjectName("CounterUn")

        self.ChPass = QtWidgets.QLineEdit(Dialog)
        self.ChPass.setGeometry(QtCore.QRect(30, 40, 241, 27))
        self.ChPass.setObjectName("ChPass")

        self.ChPass1 = QtWidgets.QLineEdit(Dialog)
        self.ChPass1.setGeometry(QtCore.QRect(30, 100, 241, 27))
        self.ChPass1.setObjectName("ChPass")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Личный кабинет"))
        self.label.setText(_translate("Dialog", "Номер региона и занимаемая площадь"))
        self.label_2.setText(_translate("Dialog", "Введите пароль"))
        self.label_3.setText(_translate("Dialog", "Повторите пароль"))
        self.button.setText(_translate("Dialog", "Изменить пароль"))
        self.buttonBox.setText(_translate("Dialog", "Выход"))
        self.CounterUn.setText(_translate("Dialog", "Добавить счетчик"))

