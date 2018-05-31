from PyQt5.QtWidgets import QDialog
from database import create_debug_engine, create_session

from Casher.View.Plateg_m import Ui_Dialog

class Company_view(QDialog):


	def get_id(self):
		return self.user_id


	model = property(get_id)


	def __init__(self, user_id):
		super(Company_view, self).__init__()
		self.user_id = user_id
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.controller = Company_controller(self)


class Company_controller:

	def __init__(self, view):
		self.view = view
		ui = view.ui
		self.user_id = view.model
		ui.pushButton.pressed.connect(self.apply)
		ui.pushButton_2.pressed.connect(self.cancel)
		ui.pushButton_3.pressed.connect(self.ok)

	def line(self):
		self.a = self.view.ui.lineEdit.text()
		self.b = self.view.ui.lineEdit_2.text()
		self.c = self.view.ui.lineEdit_3.text()
		sign = ", \\ ] [ ) ( ) > < : ; \' \" ! @ # $ % ^ & * № ` ~ { }"
		sign = sign.split()
		if self.a == "":
			self.err = "Введите ФИО"
			# return self.view.ui.label_4.setText(self.err)
		if self.b == "":
			self.err = "Введите наименование"
			# return self.view.ui.label_4.setText(self.err)

		if self.c == "":
			self.err = "Введите платеж"
			# return self.view.ui.label_4.setText(self.err)
		for i in sign:
			self.c = self.c.replace(i, ".")
		try:
			self.c = float(self.c)
			self.err = (self.a, self.b, self.c)
		except ValueError:
			self.err = "Введите число!!"
		return self.err
		# return (self.a, self.b, self.c)
	def apply(self):
		from Casher.Casher import CasherAPI
		self.api = CasherAPI(self.user_id)
		self.data = self.line()
		print(self.data)
		if type(self.data)==str:
			return self.view.ui.label_4.setText(self.err)
		self.valid = self.api.companyPay(self.data[0], self.data[1], self.data[2])
		if type(self.valid)==str:
			return self.view.ui.label_4.setText(self.valid)
		else:
			session.add(self.api.companyPay(self.data[0], self.data[1], self.data[2]))
			session.commit()

	def cancel(self):
		self.view.close()
	def ok(self):
		self.apply()
		self.cancel()


de = create_debug_engine(True)
session = create_session(de)
