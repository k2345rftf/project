from PyQt5.QtWidgets import QWidget
from Director.View.Region import Ui_Form
class Region(QWidget):
	"""docstring for Inventory"""

	def __init__(self):
		super(Region, self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.controller = Region_controller(self)

class Region_controller:
	def __init__(self, view):
		self.view = view
		ui = view.ui
		ui.pushButton_2.pressed.connect(self.new_reg)

	def line(self):
		sign = ", \\ ] [ ) ( ) > < : ; \' \" ! @ # $ % ^ & * № ` ~ { }"
		sign = sign.split()
		self.a = self.view.ui.lineEdit_3.text()

		for self.i in sign:
			self.a = self.a.replace(self.i,".")


		try:
			self.a = float(self.a)
			return self.a
		except:
			self.view.ui.label_7.setText("Пожалуйста, введите числовое значение в поле!!!")
			return None

	def new_reg(self):
		from Director.Director import InsertDirectorAPI
		from database import create_debug_engine, create_session
		de = create_debug_engine(True)
		session = create_session(de)

		self.api = InsertDirectorAPI()
		self.d = self.line()
		if self.d == None:
			return 0
		self.api.insertRegion(self.d)
		session.commit()
