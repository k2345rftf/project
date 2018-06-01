from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

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