import sys
from database import create_debug_engine, create_session
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import codecs
from Login.ControllerLog import login
from Gardener.View.Garden_main import Ui_MainWindow

        
class Gardener(QMainWindow):


    def get_id(self):
        return self.user_id

    model = property(get_id)



    def __init__(self, user_id):
        super(Gardener, self).__init__()
        self.user_id = user_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = Garden_Controller(self)



class Garden_Controller:


    def __init__(self, view):
        self.user_id = view.model
        self.view = view
        ui = view.ui
        user_id = view.model

        ui.enter.pressed.connect(self.button)
        ui.action_2.triggered.connect(self.room)
        ui.action_3.triggered.connect(self.count)


    def button(self):
        from PyQt5.QtWidgets import QTableWidgetItem

        self.b = self.parametr()
        if len(self.b) == 0:
            return 0
        self.table = self.view.ui.TableView
        self.table.clear()
        self.row = 20
        self.cols = 10
        if self.cols >= len(self.b):
            self.table.setColumnCount(self.cols)
        else:
            self.table.setColumnCount(len(self.b))
        if self.row >= len(self.b[0]):
            self.table.setRowCount(self.row)
        else:
            self.table.setRowCount(len(self.b[0]))
        self.name = ["Дата платежа","Наименование","Цена за единицу","Цена","платеж","переплата","Итог"]
        for j in range(len(self.name)):
            
            self.table.setHorizontalHeaderItem(j,QTableWidgetItem(str(self.name[j])))
        for i in range(len(self.b)):
            
            for j in range(len(self.b[i])):

                self.table.setItem(i , j, QTableWidgetItem(str(self.b[i][j])))
        self.table.resizeColumnsToContents()


    def parametr(self):
        from Gardener.Gardener import GardenerAPI
        import datetime
        self.b = GardenerAPI(self.user_id)
        self.date = []
        self.date.append(str(self.view.ui.dateEdit.text()))
        self.date.append(str(self.view.ui.dateEdit1.text()))

        if str(self.date[0]) in str(self.date[1]) and str(self.date[1]) in "01.01.2000":
            self.c = self.b.showHistory(self.user_id)

        else:
            self.view.ui.TableView.clear()
            self.date1 = self.date[0].split(".")
            self.date2 = self.date[1].split(".")
            self.c = self.b.showHistory(self.user_id, datetime.datetime(int(self.date1[2]), int(self.date1[1]),int(self.date1[0])),
            datetime.datetime(int(self.date2[2]),int(self.date2[1]),int(self.date2[0])))
        return self.c


    def count(self, event):
        from Gardener.counter import Counter_main
        self.dialog = Counter_main(self.user_id)
        self.dialog.show()


    def room(self, event):
        from Gardener.Room import Room_main, Room_mainControl
        from Gardener.Gardener import GardenerAPI
        self.api = GardenerAPI(self.user_id)
        self.o = self.api.showShare(self.user_id)
        # self.g = Room_mainControl(self.b)
        self.j = Room_main(self.user_id, self.o)
        self.j.show()


class Casher(QMainWindow):
    def get_id(self):
        return self.user_id

    model = property(get_id)

    def __init__(self, user_id):
        self.user_id = user_id
        super(Casher, self).__init__()
        self.wind()


    def wind(self):
        from Casher.View.Main_window import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = Casher_controller(self)


class Casher_controller:

    def __init__(self, view):
        self.view = view
        ui = view.ui
        self.user_id = view.model

        ui.pushButton.pressed.connect(self.button)
        ui.action.triggered.connect(self.comp)
        ui.action_2.triggered.connect(self.payment)
        ui.action_3.triggered.connect(self.gard)

    def line(self):
        return (self.view.ui.dateEdit.text(), self.view.ui.dateEdit_2.text())

    def button(self):
        from PyQt5.QtWidgets import QTableWidgetItem

        self.b = self.parametr()
        if len(self.b) == 0:
            return 0
        self.table = self.view.ui.tableWidget
        self.table.clear()
        self.row = 20
        self.cols = 10
        if self.cols >= len(self.b):
            self.table.setColumnCount(self.cols)
        else:
            self.table.setColumnCount(len(self.b))
        if self.row >= len(self.b[0]):
            self.table.setRowCount(self.row)
        else:
            self.table.setRowCount(len(self.b[0]))
        self.name = ["Дата","ФИО","Наименование услуги","Цена"]
        for j in range(len(self.name)):
            
            self.table.setHorizontalHeaderItem(j,QTableWidgetItem(str(self.name[j])))
        for i in range(len(self.b)):
            
            for j in range(len(self.b[i])):

                self.table.setItem(i , j, QTableWidgetItem(str(self.b[i][j])))
        self.table.resizeColumnsToContents()


    def parametr(self):
        from Casher.Casher import CasherAPI
        import datetime
        self.b = CasherAPI(self.user_id)
        self.date = self.line()

        if str(self.date[0]) in str(self.date[1]) and str(self.date[1]) in "01.01.2000":
            self.c = self.b.showHistory()

        else:
            self.view.ui.tableWidget.clear()
            self.date1 = self.date[0]
            self.date2 = self.date[1]
            self.c = self.b.showHistory(self.date[0], self.date[1])
        return self.c
    def comp(self):
        from Casher.Company_m import Company_view
        self.v = Company_view(self.user_id)
        self.v.show()
    def payment(self):
        from Casher.Payment_m import Payment_view
        self.v = Payment_view(self.user_id)
        self.v.show()
    def gard(self):
        self.v = Gardener(self.user_id)
        self.v.show()


class Director(QMainWindow):


    def get_id(self):
        return self.user_id


    model = property(get_id)


    def __init__(self, user_id):
        self.user_id = user_id
        super(Director, self).__init__()
        self.wind()


    def wind(self):
        from Director.View.Main_window import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = Director_Controller(self)
        # self.controller.vieww()


class Director_Controller:


    def __init__(self, view):
        self.view = view
        self.user_id = view.model
        ui = view.ui
        ui.comboBox.activated.connect(self.line)
        ui.pushButton.pressed.connect(self.button)
        ui.pushButton1.pressed.connect(self.button1)
        ui.action.triggered.connect(self.newuser)
        ui.action_2.triggered.connect(self.inventory)
        ui.action_3.triggered.connect(self.region)
        ui.action_4.triggered.connect(self.share)
        ui.action_5.triggered.connect(self.see)
        ui.action_6.triggered.connect(self.smth)
        self.vieww()


    def line(self):
        self.text = self.view.ui.comboBox.currentText()
        if self.text == "История регионов" or self.text=="Платежи предприятия":
            self.view.ui.widget.show()
            self.view.ui.widget1.hide()
            self.tables(self.text)
        elif self.text=="История платежей":
            self.view.ui.lineEdit1.setText("Введите №региона")
            self.view.ui.lineEdit1_2.setText("Введите имя")
            self.view.ui.widget1.show()
            self.view.ui.widget.hide()
            self.tables(self.text)
        else:
            self.view.ui.widget.hide()
            self.view.ui.widget1.hide()
            self.tables(self.text)
        return self.text


    def parametr(self, text, *args):
        import datetime
        self.text = text
        self.args = args

        from Director.Director import ShowDirectorAPI
        self.api = ShowDirectorAPI()
        if self.text == "История регионов" or self.text == "Платежи предприятия":

            if len(self.args)!=0 and self.args[0]!='':
                
                self.date1 = self.args[0].split(".")
                
                self.date2 = self.args[1].split(".")
                if self.text == "Платежи предприятия":
                    self.c = self.api.showComp(datetime.datetime(int(self.date1[2]), int(self.date1[1]),int(self.date1[0])),
                datetime.datetime(int(self.date2[2]),int(self.date2[0]),int(self.date2[0])))
                else:
                    self.c = self.api.showHist(datetime.datetime(int(self.date1[2]), int(self.date1[1]),int(self.date1[0])),
                    datetime.datetime(int(self.date2[2]),int(self.date2[0]),int(self.date2[0]))) 
                return self.c
            elif self.text == "Платежи предприятия":
                self.c = self.api.showComp()
            else:
                self.c = self.api.showHist()             
            return self.c
        elif self.text == "Должники":
            return self.api.showDebt()
        elif self.text == "История платежей":
            self.data = []
            if len(self.args)!=0:
                
                self.data.append(str(self.args[0]))
                self.data.append(str(self.args[1]))
            else:

                self.data.append("Введите №региона")
                self.data.append("Введите имя")
            if self.data[0]=="Введите №региона" or self.data[1] == "Введите имя":

                return self.api.showData()
            else:

                return self.api.showData(full_name=self.data[1], number_region=self.data[0])

        else:
            return self.api.showInvent()


    def vieww(self):
        self.text ="История платежей"
        self.view.ui.widget1.show()
        self.view.ui.widget.hide()
        self.view.ui.lineEdit1.setText("Введите №региона")
        self.view.ui.lineEdit1_2.setText("Введите имя")

        self.tables(self.text)


    def tables(self, text, *args):
        self.args = args

        self.table = self.view.ui.tableWidget
        self.table.clear()
        self.text = text
        

        from PyQt5.QtWidgets import QTableWidgetItem
        if len(self.args) == 0:

            self.b= self.parametr(self.text)
        else:

            self.b= self.parametr(self.text, self.args[0], self.args[1])


        self.row = 20
        self.cols = 10
        if self.text == "История платежей":
            self.name = ["ФИО","Дата платежа","Наименование","Цена за единицу","Цена","платеж","переплата","Итог"]
        elif self.text =="Должники":
            self.name = ["ФИО","Наименование","Задолженность"]
        elif self.text == "Инвентарь":
            self.name = ["Дата", "Инвентарный номер", "Наименование", "Наличие"]
        elif self.text =="История регионов":
            self.name = ["Дата покупки", "Номер участка", "ФИО покупателя", "занимаемая площадь"]
        else:
            self.name = ["Дата","ФИО","Наименование услуги","Цена"]



        if len(self.b) ==0:
            self.table.setColumnCount(self.cols)
            self.table.setRowCount(self.row)
            return 0
        else:
            if self.cols >= len(self.b):
                self.table.setColumnCount(self.cols)
            else:
                self.table.setColumnCount(len(self.b))
            if self.row >= len(self.b[0]):
                self.table.setRowCount(self.row)
            else:
                self.table.setRowCount(len(self.b[0]))
        for i in range(len(self.name)):
            self.table.setHorizontalHeaderItem(i,QTableWidgetItem(str(self.name[i])))
        for i in range(len(self.b)):
            
            for j in range(len(self.b[i])):
                
                self.table.setItem(i , j, QTableWidgetItem(str(self.b[i][j])))
        self.table.resizeColumnsToContents()


    def button(self):
        self.a = ""
        self.b = ""
        self.table = self.view.ui.tableWidget
        self.table.clear()
        self.a=self.view.ui.lineEdit.text()
        self.b=self.view.ui.lineEdit_2.text()
        self.text = self.line()
        self.tables(self.text, self.a, self.b)


    def button1(self):
        
        self.table = self.view.ui.tableWidget
        self.u=self.view.ui.lineEdit1.text()
        self.e=self.view.ui.lineEdit1_2.text()
        self.text = self.line()
        self.view.ui.tableWidget.clear()
        self.tables(self.text, self.u, self.e)


    def newuser(self):
        from Director.NewUser import NewUser 
        self.dialog = NewUser()
        self.dialog.show()


    def inventory(self):
        from Director.Inventory import Inventory 
        self.dialog = Inventory()
        self.dialog.show()


    def share(self):
        from Director.Share import Share 
        self.dialog = Share(self.user_id)
        self.dialog.show()


    def region(self):
        from Director.Region import Region 
        self.dialog = Region()
        self.dialog.show()


    def smth(self):
        self.g = Gardener("-11")
        self.g.show()
    def see(self):
        self.g = Gardener(self.user_id)
        self.g.show()





class Accountant(QMainWindow):


    def get_id(self):
        return self.user_id

    model = property(get_id)


    def __init__(self, user_id):
        self.user_id = user_id
        super(Accountant, self).__init__()
        self.wind()


    def wind(self):
        from Accountant.View.Main_window import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = Accountant_controller(self)


class Accountant_controller:


    def __init__(self, view):
        self.view = view
        ui = view.ui
        self.user_id = view.model

        ui.action.triggered.connect(self.insert)
        ui.action_2.triggered.connect(self.cash)
        ui.action_3.triggered.connect(self.gard)
        ui.comboBox.activated.connect(self.line)
        ui.pushButton.pressed.connect(self.button)


    def insert(self):
        from Accountant.Insert_main import InsertService
        self.a = InsertService()
        self.a.show() 


    def line(self):
        self.b = self.view.ui.comboBox.currentText()
        return self.b



    def button(self):        
        from PyQt5.QtWidgets import QTableWidgetItem
        self.b = self.parametr()
        if len(self.b) == 0:
            return 0
        self.table = self.view.ui.tableWidget
        self.table.clear()
        self.row = 20
        self.cols = 10
        if self.cols >= len(self.b):
            self.table.setColumnCount(self.cols)
        else:
            self.table.setColumnCount(len(self.b))
        if self.row >= len(self.b[0]):
            self.table.setRowCount(self.row)
        else:
            self.table.setRowCount(len(self.b[0]))
        # self.name = ["Дата платежа","Наименование","Цена за единицу","Цена","платеж","переплата","Итог"]
        for i in range(len(self.b)):
            
            for j in range(len(self.b[i])):
                # self.table.setHorizontalHeaderItem(j,QTableWidgetItem(str(self.name[j])))
                self.table.setItem(i , j, QTableWidgetItem(str(self.b[i][j])))


    def parametr(self):
        from Accountant.Accountent import AccountentAPI
        import datetime
        self.api = AccountentAPI()
        self.date = []
        self.date.append(str(self.view.ui.dateEdit.text()))
        self.date.append(str(self.view.ui.dateEdit_2.text()))
        self.text = self.line()

        if str(self.date[0]) in str(self.date[1]) and str(self.date[1]) in "01.01.2000":
            if self.text!="Услуги":
                self.c = self.api.showCompany()
            else:
                self.c = self.api.showService()

        else:
            self.view.ui.tableWidget.clear()
            self.date1 = self.date[0]
            self.date2 = self.date[1]
            if self.text=="Услуги":
                self.c = self.api.showService(self.date1, self.date2)

            else:

                self.c = self.api.showCompany(self.date1, self.date2)
        return self.c
    def cash(self):
        self.v = Casher(self.user_id)
        self.v.show()

    def gard(self):
        self.v = Gardener(self.user_id)
        self.v.show()



        
class Control:


    def __init__(self, *args):
        super(Control, self).__init__()
        self.event = args
        self.priv = {"0": Gardener}
    

    @classmethod
    def check(self, *args):
        self.event = args
        print(self.event)
        from Observer import Windows
        self.win = Windows()
        self.login = login()
        if len(self.event) != 0:
            
            if self.event[0][0][0] == 0:
                self.main_window = Gardener(self.event[0][1])
                self.win.run(self.main_window)
                
            elif self.event[0][0][0] == 1:
                self.main_window = Casher(self.event[0][1])
                self.win.run(self.main_window)
                
            elif self.event[0][0][0] == 2:
                self.main_window = Director(self.event[0][1])
                self.win.run(self.main_window)
            
            elif self.event[0][0][0] == 3:
                self.main_window = Accountant(self.event[0][1])
                self.win.run(self.main_window)
        else:
            self.win.run(self.login) 




if __name__ == '__main__':

    de = create_debug_engine(True)
    session = create_session(de)
    app = QApplication(sys.argv)
    w = Control.check()
    session.commit()
    app.exec_()