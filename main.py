﻿import sys
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
        print(self.b)
        if len(self.b) == 0:
            return 0
        self.table = self.view.ui.TableView
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
            datetime.datetime(int(self.date2[2]),int(self.date2[0]),int(self.date2[0])))
        return self.c
    def count(self, event):
        from Gardener.counter import Counter_main
        self.dialog = Counter_main(self.user_id)
        self.dialog.show()
    def room(self, event):
        from Gardener.Room import Room_main, Room_mainControl
        from Gardener.Gardener import GardenerAPI
        self.api = GardenerAPI(self.user_id)
        self.b = self.api.showShare(self.user_id)
        # self.g = Room_mainControl(self.b)
        self.j = Room_main(self.user_id, self.b)
        self.j.show()


class Casher(QMainWindow):
    def __init__(self, user_id):
        self.user_id = user_id
        super(Casher, self).__init__()
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
    # w = Control.check()
    w = Gardener("1")
    w.show()
    app.exec_()