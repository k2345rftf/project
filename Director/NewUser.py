from PyQt5.QtWidgets import QWidget
from Director.View.Registr import Ui_Form
class NewUser(QWidget):
	"""docstring for Inventory"""
	def __init__(self):
		super(NewUser, self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.controller = Newuser_controller(self)

class Newuser_controller:
	def __init__(self, view):
		self.view = view
		ui = view.ui
		ui.pushButton.pressed.connect(self.ok)
		ui.pushButton_2.pressed.connect(self.accept)
		ui.pushButton_3.pressed.connect(self.cancel)
	def line(self):
		self.a = self.view.ui.comboBox.currentText()
		self.b = self.view.ui.comboBox_2.currentText()
		if self.a == "Да":
			self.a = 1
		else:
			self.a=0
		if self.b == "Да":
			self.b = 1
		else:
			self.b=0
		return (self.view.ui.lineEdit.text(), self.view.ui.lineEdit_2.text(),self.view.ui.lineEdit1.text(), self.a, self.b)
	def ok(self):
		from Director.Director import InsertDirectorAPI
		from database import create_debug_engine, create_session
		de = create_debug_engine(True)
		session = create_session(de)
		self.api = InsertDirectorAPI()
		self.data = self.line()
		if self.data[0] == "":
			return self.view.close()
		session.add(self.api.insertUser(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4]))
		session.commit()
		return self.view.close()
	def accept(self):
		from Director.Director import InsertDirectorAPI
		from database import create_debug_engine, create_session
		de = create_debug_engine(True)
		session = create_session(de)
		self.api = InsertDirectorAPI()
		self.data = self.line()
		if self.data[0] == "":
			return self.view.ui.label12.setText("Пожалуйста, заполните все поля!!!")
		self.n = self.api.insertUser(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4])
		if type(self.n) == str:
			return self.view.ui.label12.setText(self.n)
		session.add(self.n)
		return session.commit()

	def cancel(self):
		return self.view.close()
