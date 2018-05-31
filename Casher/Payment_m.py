from PyQt5.QtWidgets import QDialog
from database import create_debug_engine, create_session

from Casher.View.Payment_m import Ui_Dialog

class Payment_view(QDialog):


	def get_id(self):
		return self.user_id


	model = property(get_id)


	def __init__(self, user_id):
		super(Payment_view, self).__init__()
		self.user_id = user_id
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.controller = Payment_controller(self)


class Payment_controller:

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
		self.d = self.view.ui.lineEdit_4.text()
		self.e = self.view.ui.lineEdit_5.text()
		sign = ", \\ ] [ ) ( ) > < : ; \' \" ! @ # $ % ^ & * № ` ~ { }"
		sign = sign.split()
		if self.a == "":
			self.err = "Введите ФИО"
			# return self.view.ui.label_4.setText(self.err)
		if self.b == "":
			self.err = "Введите номер региона"
			# return self.view.ui.label_4.setText(self.err)

		if self.c == "":
			self.err = "Введите название услуги"
			# return self.view.ui.label_4.setText(self.err)
		if self.d == "":
			self.err = "Введите платеж"
			# return self.view.ui.label_4.setText(self.err)
		if self.e == "":
			self.err = "Введите усредненное значение(если есть счетчик, то введите \"Счетчик\")"
			# return self.view.ui.label_4.setText(self.err)
		for i in sign:
			self.b = self.b.replace(i, ".")
			self.d = self.d.replace(i, ".")
			self.e = self.e.replace(i, ".")
		try:
			self.d = float(self.d)
			self.b = float(self.b)
			self.e = float(self.e)
			self.err = (self.a, self.b, self.c, self.d, self.e)
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
			return self.view.ui.label_6.setText(self.data)
		self.valid = self.api.gardenerPay(self.user_id, self.data[0], self.data[1], self.data[2], self.data[3], self.data[4])
		if type(self.valid)==str:
			return self.view.ui.label_6.setText(self.valid)
		else:
			session.add(self.valid)
			session.commit()

	def cancel(self):
		self.view.close()
	def ok(self):
		self.apply()
		self.cancel()


de = create_debug_engine(True)
session = create_session(de)