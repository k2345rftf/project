# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Counter.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Counter(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 376)
        Dialog.setMinimumSize(QtCore.QSize(495, 376))
        Dialog.setMaximumSize(QtCore.QSize(495, 376))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 351, 17))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 70, 441, 41))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 351, 27))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("") 
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(70, 110, 271, 27))
        self.doubleSpinBox.setMaximum(9999999999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.typeCounter = QtWidgets.QLineEdit(Dialog)
        self.typeCounter.setGeometry(QtCore.QRect(70, 70, 271, 27))
        self.typeCounter.setObjectName("typeCounter")
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Показания счетчика"))
        self.label.setText(_translate("Dialog", "Введите данные приборов учета"))
        self.typeCounter.setText(_translate("Dialog", "Введите наименование услуги"))
