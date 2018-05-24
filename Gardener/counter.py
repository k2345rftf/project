import sys, os.path
direct = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '//')
sys.path.append(direct)
from PyQt5.QtWidgets import QApplication, QDialog

from Gardener.View.counterUI import Counter

class Counter_main(QDialog):
	def __init__(self):
		super(Counter_main, self).__init__()
		self.ui = Counter()
		self.ui.setupUi(self)
