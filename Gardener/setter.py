import sys, os.path
direct = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '//')
sys.path.append(direct)
from PyQt5.QtWidgets import QDialog

class SetCounterView(QDialog):
	def get_id(self):
		return self.user_id
	model = property(get_id)
	def __init__(self, user_id):
		super(SetCounterView, self).__init__()
		self.user_id = user_id
		self.view()
	def view(self):
		from Gardener.View.setCounter import SetCounter
		self.ui = SetCounter()
		self.ui.setupUi(self)
		self.controller = Controller_setCount(self)


class Controller_setCount:
	def __init__(self, view):
		self.view = view
		self.user_id = view.model
		ui = view.ui
		ui.buttonBox.accepted.connect(self.button)

	def button(self):
		from Gardener.Gardener import GardenerAPI
		self.view.ui.label_3.setText("")
		self.a = GardenerAPI(self.user_id)
		self.cl = self.view.ui.classAccur.text()
		self.tp = self.view.ui.typeCounter.text()
		self.r = self.a.addCounter(self.tp, self.cl)
		if type(self.r) == str:
			self.error(self.r)

	def error(self, err):
		self.err = err
		self.view.ui.label_3.setText(self.err)