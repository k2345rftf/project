from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


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