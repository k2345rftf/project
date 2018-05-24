import sys
from database import create_debug_engine, create_session
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import codecs
from Login.ControllerLog import login


        
class Gardener(QMainWindow):
    def __init__(self, user_id):
        super(Gardener, self).__init__()
        self.user_id = user_id
        self.wind()
    def wind(self):
        from Gardener.View.Garden_main import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.smth = self.ui.setupUi(self)
        self.ui.enter.pressed.connect(self.button)
        self.ui.action_2.triggered.connect(self.room)
        self.ui.action_3.triggered.connect(self.count)
    def button(self):
        from PyQt5.QtWidgets import QTableWidgetItem
        self.b = self.parametr()
        self.table = self.ui.TableView
        self.table.clear()
        self.row = len(self.b)
        self.cols = len(self.b[0])
        self.table.setColumnCount(self.cols)
        self.table.setRowCount(self.row)
        self.name = ["Дата платежа","Наименование","Цена за единицу","Цена","платеж","переплата","Итог"]
        for i in range(len(self.b)-1):
            
            for j in range(len(self.b[i])):
                self.table.setHorizontalHeaderItem(j,QTableWidgetItem(str(self.name[j])))
                self.table.setItem(i+1 , j, QTableWidgetItem(str(self.b[i+1][j])))
    def parametr(self):
        from Gardener.Gardener import GardenerAPI
        self.b = GardenerAPI(self.user_id)
        self.c = self.b.showHistory(self.user_id)
        return self.c
    def count(self, event):
        from Gardener.counter import Counter_main
        self.dialog = Counter_main()
        self.dialog.show()
    def room(self, event):
        from Gardener.Room import Room_main
        self.dialog = Room_main()
        self.dialog.show()


class Casher(QMainWindow):
    def __init__(self, user_id):
        super(Casher, self).__init__()
        self.user_id = user_id
        # self.wind()
    def wind(self):
        from Casher.View.Casher_main import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Director(QMainWindow):
    def __init__(self, user_id):
        self.user_id = user_id
        super(Director, self).__init__()
        self.wind()
    def wind(self):
        from Director.View.Director_main import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Accountant(QMainWindow):
    def __init__(self, user_id):
        self.user_id = user_id
        super(Accountant, self).__init__()
        self.wind()
    def wind(self):
        from Accountant.View.Accountant_main import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class HiredWorker(QMainWindow):
    def __init__(self, user_id):
        self.user_id = user_id
        super(HiredWorker, self).__init__()
        self.wind()
    def wind(self):
        from HiredWorker.View.HiredWorker_main import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
class Control:
    def __init__(self, *args):
        super(Control, self).__init__()
        self.event = args
        self.priv = {"0": Gardener}
    @classmethod
    def check(self, *args):
        self.event = args
        from Observer import Windows
        self.win = Windows()
        self.login = login()
        print(self.event)
        if len(self.event) != 0:
            
            if self.event[0][0] == 0:
                self.main_window = Gardener(self.event[0][1])
                self.win.run(self.main_window)
                
            elif self.event[0][0] == 1:
                self.main_window = Casher(self.event[0][1])
                self.win.run(self.main_window)
                
            elif self.event[0][0] == 2:
                self.main_window = Director(self.event[0][1])
                self.win.run(self.main_window)
            
            elif self.event[0][0] == 3:
                self.main_window = Accountant(self.event[0][1])
                self.win.run(self.main_window)
            
            elif self.event[0][0] == 4:
                self.main_window = HiredWorker(self.event[0][1])
            
                self.win.run(self.main_window)
        
        else:
            
            self.win.run(self.login) 




if __name__ == '__main__':
    de = create_debug_engine(True)
    session = create_session(de)
    app = QApplication(sys.argv)
    w = Control.check()
    # w = Gardener("1")
    # w.show()
    app.exec_()