from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
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