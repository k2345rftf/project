import sys, os.path
direct = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '//')
sys.path.append(direct)
from PyQt5.QtWidgets import QApplication, QDialog

from Gardener.View.counterUI import Counter

class Counter_main(QDialog):
	def get_id(self):
		return self.user_id
	# count = property(get_count)
	model = property(get_id)
	def __init__(self, user_id):
		super(Counter_main, self).__init__()
		self.user_id = user_id
		self.ui = Counter()
		self.ui.setupUi(self)
		self.controller = Controller_counter(self)


class Controller_counter:
	"""docstring for Controller_counter"""
	def __init__(self, view):
		super(Controller_counter, self).__init__()
		self.view = view
		self.user_id = view.model
		ui = view.ui
		ui.buttonBox.accepted.connect(self.button)
		# self.button()

	def button(self):		
		from Gardener.Gardener import GardenerAPI
		self.g = GardenerAPI(self.user_id)
		self.text = self.view.ui.typeCounter.text()
		if self.g.checkCounter(self.text) == False:
			self.value = self.view.ui.doubleSpinBox.value()
			if type(self.g.insertCounter(self.user_id, self.value, self.text)) == str:
				self.view.ui.label_2.setText(self.g.insertCounter(self.user_id, self.value, self.text))	
		else:
			self.view.ui.label_2.setText(self.g.checkCounter(self.text))

