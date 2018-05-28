from PyQt5.QtWidgets import QWidget
from Director.View.setShare import Ui_Form
class Share(QWidget):
	"""docstring for Inventory"""
	def get_id(self):
		return self.user_id
	model = property(get_id)

	def __init__(self, user_id):
		super(Share, self).__init__()
		self.ui = Ui_Form()
		self.user_id = user_id
		self.ui.setupUi(self)
		self.controller = Share_controller(self)

class Share_controller:
	def __init__(self, view):
		self.view = view
		ui = view.ui
		self.user_id = view.model
		ui.pushButton.pressed.connect(self.accept)
		ui.pushButton_2.pressed.connect(self.cancel)
	def line(self):
		sign = ", \\ ] [ ) ( ) > < : ; \' \" ! @ # $ % ^ & * № ` ~ { }"
		sign = sign.split()
		self.a = self.view.ui.lineEdit_2.text()

		for self.i in sign:
			self.a = self.a.replace(self.i,".")


		try:
			self.b = int(self.view.ui.lineEdit_3.text())
			self.a = float(self.a)
			return (self.view.ui.lineEdit.text(), self.a,self.b, self.view.ui.lineEdit_4.text())
		except:
			return self.view.ui.label_5.setText("Пожалуйста, введите числовое значение в поле!!!")

	def accept(self):
		from Director.Director import InsertDirectorAPI
		from database import create_debug_engine, create_session
		de = create_debug_engine(True)
		session = create_session(de)
		self.api = InsertDirectorAPI()
		self.data = self.line()
		if self.data == None:
			return 0
		if self.data[0] == "":
			return self.view.ui.label_5.setText("Пожалуйста, заполните все поля!!!")
		self.n = self.api.insertShare(self.user_id, self.data[0], self.data[1], self.data[2], self.data[3])
		if type(self.n) == str:
			return self.view.ui.label_5.setText(self.n)
		if self.n ==0:
			return self.view.ui.label_5.setText("Данные обновлены") 
		session.add(self.n)
		return session.commit()

	def cancel(self):
		return self.view.close()