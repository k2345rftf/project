from PyQt5.QtWidgets import QWidget
from Director.View.setInventory import Ui_Form
class Inventory(QWidget):
	"""docstring for Inventory"""
	def __init__(self):
		super(Inventory, self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.controller = Inventory_controller(self)


class Inventory_controller:
	def __init__(self, view):
		self.view = view
		ui = view.ui
		ui.pushButton.pressed.connect(self.button)

	def button(self):
		from Director.Director import InsertDirectorAPI
		self.value = self.view.ui.lineEdit.text()
		if self.value == "":
			return 0
		self.api = InsertDirectorAPI()
		self.api.insertInv(self.value)

		