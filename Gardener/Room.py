import sys, os.path
direct = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '//')
sys.path.append(direct)
from PyQt5.QtWidgets import QApplication, QDialog

from Gardener.View.MyRoom import Ui_Dialog

class Room_main(QDialog):
	def __init__(self):
		super(Room_main, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.buttonbox.connect
