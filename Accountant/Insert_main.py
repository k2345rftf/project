from Accountant.View.Insert import Ui_Form
from PyQt5.QtWidgets import QWidget
from database import create_debug_engine, create_session


class InsertService(QWidget):

    def __init__(self):
        super(InsertService, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.controller = Insert_controller(self)


class Insert_controller:


    def __init__(self, view):
        self.view = view
        ui = view.ui

        ui.pushButton.pressed.connect(self.ok)
        ui.pushButton_2.pressed.connect(self.accept)
        ui.pushButton_3.pressed.connect(self.cancel)

    def line(self):
        self.err = ""
        sign = ", \\ ] [ ) ( ) > < : ; \' \" ! @ # $ % ^ & * № ` ~ { }"
        sign = sign.split()
        self.q1 = self.view.ui.lineEdit.text()
        self.q2 = self.view.ui.lineEdit_2.text()
        self.q3 = self.view.ui.lineEdit_3.text()
        self.q4 = self.view.ui.lineEdit_4.text()
        self.q5 = self.view.ui.lineEdit_7.text()
        self.q6 = self.view.ui.lineEdit_5.text()
        self.q7 = self.view.ui.lineEdit_6.text()
        self.q8 = self.view.ui.lineEdit_8.text()
        self.a = (self.q1,self.q2,self.q3,self.q7,self.q4,self.q5,self.q6,self.q8)
        if self.a[0] =="":
            self.err ="Введите название услуги"
            return self.view.ui.label_9.setText(self.err)
        elif self.a[1] =="":
            
            self.err ="Введите наименование документа"
            return self.view.ui.label_9.setText(self.err)
        elif self.a[2] == "01.01.2000":
            self.err = "Введите дату документа"
            return self.view.ui.label_9.setText(self.err)
        elif self.a[7] =="01.01.2000":
            self.err = "Введите дату пени!!"
            return self.view.ui.label_9.setText(self.err)
        elif self.a[3] =="":
            self.err = "Введите период начисления"
            return self.view.ui.label_9.setText(self.err)
        elif self.a[4] =="":
            self.err = "Введите Цену за единицу"
            return self.view.ui.label_9.setText(self.err)
        elif self.a[5] =="":
            self.err = "Введите Единицы измерения"
            return self.view.ui.label_9.setText(self.err)
        elif self.a[6] =="":
            self.err = "Введите пени(в процентах)"
            return self.view.ui.label_9.setText(self.err)
        for i in sign:
            self.a4 = self.a[3].replace(i, ".")
            self.a5 =self.a[4].replace(i, ".")
            self.a7 =self.a[6].replace(i, ".")
        try:
            self.a4 = float(self.a4)
            self.a5 = float(self.a5)
            self.a7 = float(self.a7)
        except ValueError:
            return self.view.ui.label_9.setText("Введите число!!!")
        return self.a


    def ok(self):
        self.accept()

        self.view.close()


    def accept(self):
        from Accountant.Accountent import AccountentAPI
        self.api = AccountentAPI()
        self.data = self.line()
        if self.data == None:
            return 0
        session.add(self.api.insert_serv(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4],self.data[5],self.data[7],self.data[6]))
        session.commit()
    def cancel(self):
        self.view.close()

de = create_debug_engine(True)
session = create_session(de)