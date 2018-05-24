import sys, os.path
direct = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '//')
sys.path.append(direct)
from Login.Logining import Logining
from Observer import Observe

from Login.LoginW_UI import Login_ui
from PyQt5.QtWidgets import QApplication, QWidget
import sys






class login(QWidget):
    """docstring for View"""
    def __init__(self):
        super(login, self).__init__()
        self.ui = Login_ui()
        self.ui.setupUi(self)
        self.ui.sign_in.pressed.connect(self.user)
    def user(self):
        self.a = self.ui.login.text()
        self.b = self.ui.password.text()
        self.v = LoginController(self).user_id(self.a, self.b)
        if type(self.v) == str:
            self.error()
        else:
            self.close()

    def error(self):
        self.ui.error.setText("Error")

class LoginController(Observe):
    """docstring for Conteroller"""
    def __init__(self, view):
        super(LoginController, self).__init__()
        self.view = view
    def user_id(self, log, password):
        from database import isNone
        self.login = log
        self.password = password
        self.user = Logining.user(self.login, self.password)
        if type(self.user)== str:
            return "error"
        self.event = Logining.privelege(self.user)
        self.update(self.event, self.user[0])
        return self.user

    def update(self, *args):
        from database import isNone
        from main import Control
        self.args = args
        if len(self.args) == 0:
            self.event = 0
        else:
            self.event = self.args
        self.n = Control().check(self.event)


       

