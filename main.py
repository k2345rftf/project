import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import codecs


from database import create_debug_engine, create_session
from Login.ControllerLog import login
from Gardener.Gardener_main import Gardener
from Accountant.Accountant_main import Accountant
from Casher.Casher_main import Casher
from Director.Director_main import Director
from Observer import Windows


class Control:
    def __init__(self, *args):
        super(Control, self).__init__()
        self.event = args
        self.login = login()
        self.win = Windows()
    

    def addWind(self, name_wind, *args):
        self.user_id = args
        self.main_window = name_wind
        if len(self.user_id)!=0:
            self.win.run(self.main_window(self.user_id[0]))
        else:
            self.win.run(self.login)


    def check(self, *args):
        self.event = args
        if len(self.event) != 0:
            
            if self.event[0][0][0] == 0:
                self.addWind(Gardener,self.event[0][1])
                
            elif self.event[0][0][0] == 1:
                self.addWind(Casher,self.event[0][1])
                
            elif self.event[0][0][0] == 2:
                self.addWind(Accountant,self.event[0][1])


            elif self.event[0][0][0] == 3:
                self.addWind(Director,self.event[0][1])
        else:
            self.addWind(self.login) 




if __name__ == '__main__':

    de = create_debug_engine(True)
    session = create_session(de)
    app = QApplication(sys.argv)
    w = Control()
    w.check()
    session.commit()
    app.exec_()