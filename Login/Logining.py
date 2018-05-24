import sys, os.path
direct = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '//')
sys.path.append(direct)
from database import create_debug_engine, create_session

class Logining:
	def __init__(self, *args):
		self.args = args
	@classmethod
	def user(self, *args):
		from database import User, isNone
		self.args = args
		self.login = self.args[0]
		self.password = self.args[1]
		self.us = session.query(User.id).filter(User.login == self.login).filter(User.password == self.password).all()
		if len(self.us)==0:
			self.err = "error"
			return self.err
		else:
			self.k = []
			self.user_id = self.us[0][0]
			self.k.append(self.user_id)
			self.k.append(self.privelege(self.user_id))
			return self.user_id
	@classmethod
	def privelege(self, user_id):
		from database import User
		self.user_id = user_id
		self.priv = session.query(User.privelege).filter(User.id == self.user_id).all()
		print(self.priv[0][0])
		return self.priv[0][0]

de = create_debug_engine(True)
session = create_session(de)