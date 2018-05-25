import sys, os.path
direct = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '//')
sys.path.append(direct)
from PyQt5.QtWidgets import QApplication, QDialog
from Observer import Windows
from Gardener.View.MyRoom import Ui_Dialog
class Room_mainControl:
	def __init__(self, view):
		super(Room_mainControl, self).__init__()

		self.view = view
		self.user_id = view.user_id
		self.share = view.shares
		ui = view.ui
		ui.button.pressed.connect(self.button)
		ui.CounterUn.pressed.connect(self.button2)
		ui.buttonBox.pressed.connect(self.quit)
		# self.show()
		self.tables()
	def quit(self):
		self.view.close()
	def tables(self):
		from PyQt5.QtWidgets import QTableWidgetItem
		self.b = self.share
		self.table = self.view.ui.TableView
		self.table.clear()
		if len(self.b)!=0:
			self.row = len(self.b)
			self.cols = len(self.b[0])
			self.table.setColumnCount(self.cols)
			self.table.setRowCount(self.row)
			self.name = ["Номер региона","Занимаемая часть"]
			for i in range(len(self.b)-1):            
				for j in range(len(self.b[i])):
					self.table.setHorizontalHeaderItem(j,QTableWidgetItem(str(self.name[j])))
					self.table.setItem(i+1 , j, QTableWidgetItem(str(self.b[i+1][j])))
		else:
			self.table.removeCellWidget
			self.view.ui.label_4.setText("Вы не владеете регионом")
	def button(self):
		self.pas1 = self.view.ui.ChPass.text()
		self.pas2 = self.view.ui.ChPass1.text()
		if self.pas1 != self.pas2:
			self.error()
		if len(self.pas1) is not 0 or len(self.pas1) is not 0:
			print(1)
			self.update(self.pas1, self.pas2)
		elif len(self.pas1) is not 0:
			self.error()
	def button2(self):
		from Gardener.setter import SetCounterView
		self.v = SetCounterView(self.user_id)
		self.v.show()

	def error(self):
		self.view.ui.label_2.setText("Пароли не совпадают")

	def update(self, a, b):
		self.a = a
		from Gardener.Gardener import GardenerAPI
		print(str(self.user_id)+"============")
		self.c = GardenerAPI(self.user_id)
		self.c.changePass(self.a)


class Room_main(QDialog):
	def get_id(self):
		return self.user_id

	def get_share(self):
		return self.share

	user_ids = property(get_id)
	shares = property(get_share)
	def __init__(self, user_id, share):
		super(Room_main, self).__init__()
		self.share = share
		self.user_id = user_id
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.controller = Room_mainControl(self)


