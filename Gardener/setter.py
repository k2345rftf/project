import sys, os.path
direct = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '//')
sys.path.append(direct)
from PyQt5.QtWidgets import QDialog

class SetCounterView(QDialog):
	def __init__(self):
		super(SetCounterView, self).__init__()
		self.view()
	def view(self):
		from Gardener.View.setCounter import SetCounter
		self.ui = SetCounter()
		self.ui.setupUi(self)
