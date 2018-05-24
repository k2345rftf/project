from abc import ABCMeta, abstractmethod

class Observable(metaclass = ABCMeta): 
	"""docstring for Observable"""
	def __init__(self):
		super(Observable, self).__init__()
		self.arg = []

	def addObserve(self, inObserve):
		self.arg.append(inObserve)
	def shown(self):
		for x in self.arg:
			x.show()

class Observe:
	def __init__(self):
		pass

	@abstractmethod
	def update(self):
		pass

class Windows(Observable):

	def addWindow(self, window):
		return self.addObserve(window)
	def run(self, window):
		self.addWindow(window)
		self.shown()