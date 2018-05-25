import sys, os.path
direct = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '//')
sys.path.append(direct)
from PyQt5.QtWidgets import QApplication, QDialog

from Gardener.View.counterUI import Counter

class Counter_main(QDialog):
	def get_id(self):
		return self.user_id
	def get_count(self):
		return self.r
	count = property(get_count)
	model = property(get_id)
	def __init__(self, user_id):
		super(Counter_main, self).__init__()
		self.user_id = user_id
		self.r = Counter()
		self.ui = self.r.setupUi(self)
		self.controller = Controller_counter(self)


class Controller_counter(object):
	"""docstring for Controller_counter"""
	def __init__(self, view):
		super(Controller_counter, self).__init__()
		self.view = view
		self.user_id = view.model
		ui = view.ui
		self.button()

	def button(self):		
		from database import CounterUnit
		self.b = []
		for self.name in session.query(CounterUnit.typeCounter).filter(CounterUnit.user_id == self.user_id):
			self.b.append(self.name)
		if len(self.b) == 0:
			pass
		else:
			self.show_count(self.name)

	def show_count(self, name):
		if len(self.name) != 0:
			self.view.count.

