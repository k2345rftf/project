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
		# self.ui.ShareTable.showGrid.connect(self.table)
		self.ui.button.pressed.connect(self.button)
		self.ui.CounterUn.pressed.connect(self.button2)
		self.ui.buttonBox.pressed.connect(self.quit)
	def quit(self):
		self.close()
	def table(self):
		pass
	def button(self):
		# self.pas1 = self.ui.ChPass.text()
		# self.pas2 = self.ui.ChPass1.text()
		# ControllerRoom.update(self.pas1, self.pas2)
		pass

	def button2(self):
		print("==================================================")
		from Gardener.setter import SetCounterView
		self.v = SetCounterView()
		self.v.show()

