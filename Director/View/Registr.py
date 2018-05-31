# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registration.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setMinimumSize(QtCore.QSize(600, 400))
        Form.setMaximumSize(QtCore.QSize(600, 400))
        self.lineEdit1 = QtWidgets.QLineEdit(Form)
        self.lineEdit1.setGeometry(QtCore.QRect(40, 14, 291, 31))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 64, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 110, 291, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(40, 160, 291, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Да")
        self.comboBox.addItem("Нет")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 204, 291, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Да")
        self.comboBox_2.addItem("Нет")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 320, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 320, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 320, 131, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(350, 10, 141, 31))
        self.label1.setObjectName("label1")
        self.label12 = QtWidgets.QLabel(Form)
        self.label12.setGeometry(QtCore.QRect(100, 280, 500, 31))
        self.label12.setObjectName("label12")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 60, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 160, 251, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 110, 141, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(350, 200, 141, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Форма регистрации"))
        self.pushButton.setText(_translate("Form", "ok"))
        self.pushButton_2.setText(_translate("Form", "применить"))
        self.pushButton_3.setText(_translate("Form", "cancel"))
        self.label.setText(_translate("Form", "Введите логин"))
        self.label1.setText(_translate("Form", "Введите ФИО"))
        self.label_2.setText(_translate("Form", "Членство в садоводстве"))
        self.label_3.setText(_translate("Form", "Введите пароль"))
        self.label_4.setText(_translate("Form", "Привилегия"))

