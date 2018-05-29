from database import User, Share, Region, Company, Transactions, Service, Counter, create_debug_engine, create_session, select_obj, Inventory

import datetime




class Companies:

	def __init__(self, *date):
		self.date = date

	def show_all(self):
		self.b = []
		for self.data in session.query(Company.date,
									  User.NFC,
									  Company.name_service,
									  Company.cost).filter(User.id == Company.id_creditor):
			self.b.append(self.data)
		return self.b

	def  show_area(self):
		self.c = []
		for self.data in session.query(Company.date,
                                       User.NFC,
                                       Company.name_service,
                                       Company.cost).filter(Company.date >= self.date[0]).filter(Company.date <= self.date[1]).filter(User.id == Company.id_creditor):
			self.c.append(self.data)
		return self.c

class Inventories:
  def __init__(self, *args):
    self.args = args 
  def show_all(self):
    self.b = []
    for self.data in session.query(Inventory.date,
                                       Inventory.number_unit,
                                       Inventory.name_unit,
                                       Inventory.available):
      self.b.append(self.data)                       
            
    return self.b
        


class Debts:

  def __init__(self, *args):
    self.args = args

  def show_all(self):
    self.name_serv = []
    self.result = []

    for self.name in session.query(Service.name_service):
      if self.name[0] in self.name_serv:
        continue
      else:
        self.name_serv.append(self.name[0])
    self.users = session.query(User.id, User.NFC).all()
    for self.i in self.users:
      self.debt = 0
      for self.j in self.name_serv:
        for self.total in session.query(Transactions.total).filter(Transactions.id_user == self.i[0]).\
                                                              filter(Transactions.name_serv == self.j):
          self.debt = self.total[0]
        if self.debt < 0:
          self.result.append((self.i[1], self.j, self.debt))
                    
    return self.result


class ShowData:

  def get_table_history_payment(self, **kwargs):
    from database import User, Share, Region
    self.Full_name = kwargs.get("full_name")
    self.numb_region = kwargs.get("number_region")
    self.user_id = ""
    if (self.Full_name)==None or self.numb_region == None:
      return session.query(User.NFC,
                           Transactions.date,
                           Transactions.name_serv,
                           Transactions.cost_unit,
                           Transactions.cost,
                           Transactions.payment,
                           Transactions.overpayments,
                           Transactions.total).filter(User.id == Transactions.id_user).all()
    self.value = []

    self.ids = session.query(User.id).filter(User.NFC == self.Full_name).all()
    self.regs = session.query(Share.user_id).filter(Share.region_id == Region.region_id).filter(Region.number_region == self.numb_region).all()
    for self.i in range(len(self.ids)):
      for self.j in range(len(self.regs)):
        if self.ids[self.i][0]==self.regs[self.j][0]:
          self.user_id = str(self.ids[self.i][0])
          break
    if len(self.user_id) == 0:
      self.user_id=-2
    else:
      self.user_id=int(self.user_id)
    print(self.user_id)
    for self.history in session.query(User.NFC,
                           Transactions.date,
                           Transactions.name_serv,
                           Transactions.cost_unit,
                           Transactions.cost,
                           Transactions.payment,
                           Transactions.overpayments,
                           Transactions.total).filter(User.id == Transactions.id_user).filter(Transactions.id_user == self.user_id):
      self.value.append(self.history)

    print("+++++++++++++++++++++++")
         
    return self.value

              

class NewUser:

  def check_user(self, login):
    self.login = login
    self.user = session.query(User.id).filter(User.login == self.login).all()
    try:
      self.result = self.user[0][0]
    except IndexError:
      self.result = None
    return self.result

  def createUser(self, login, password, full_name, membership, privelege):
    from database import User, isNone
    self.login = login
    self.password = password
    self.full_name = full_name
    self.membership = membership
    self.privelege = privelege
    if isNone(self.check_user(self.login)):
      self.user_id = session.query(User.id).filter(User.id >=0).all()
      try:
        self.id = self.user_id[len(self.user_id)-1][0]
      except IndexError:
        self.id = -1

      self.b = User(
        id = self.id + 1,
        login = self.login,
        password = self.password,
        NFC = self.full_name,
        membership = self.membership,
        privelege = self.privelege,
        counter = 0
        )
      return self.b
    else:
      self.err = "Такой пользователь уже есть в системе!!!!"
      return self.err


class NewInventory:

  def __init__(self, name):
    self.name = name


  def insertInventory(self, name):
    from database import Inventory
    import datetime
    self.name = name
    self.num = session.query(Inventory.number_unit).all()
    try:
      self.number = self.num[len(self.num)-1][0]
    except IndexError:
      self.number = -1
    self.result = session.query(Inventory.name_unit).filter(Inventory.name_unit == self.name).all()

    for self.i in range(len(self.result)-1):

      if self.name in self.result[self.i]:
        session.query(Inventory).filter(Inventory.name_unit == self.name).update({"available" : 0})
    self.b = Inventory(
                        date = datetime.datetime.now(),
                        number_unit = self.number + 1,
                        name_unit = self.name,
                        available = 1

      )
    session.add(self.b)
    session.commit()


class Region_work:
  def check_region(self, number_region):
    self.number_region = number_region
    self.b = session.query(Region.number_region).filter(Region.number_region == self.number_region).all()
    if len(self.b) == 0:
      self.err = "Такого региона не существует!"
      return self.err
    else:
      return 0

  def insertRegion(self, area):
    from database import Region
    self.area = area
    self.data = session.query(Region.region_id, Region.number_region).all()
    try:
      self.reg_id = self.data[len(self.data)-1][0]+1
      self.number = self.data[len(self.data)-1][1]+1
    except IndexError:
      self.reg_id = 0
      self.number = 0
    self.b = Region(
                    region_id = self.reg_id,
                    area = self.area,
                    number_region = self.number)
    return session.add(self.b)

  def updateRegion(self, number_region, area):

    self.number_region = number_region
    self.area = area
    self.b = self.check_region(self.number_region)
    if self.b == 0:
      session.query(Region).filter(Region.number_region == self.number_region).update({"area": self.area})
    else:
      return self.b

class Share_work:
  def __init__(self, user_id):
    self.id = user_id
  def checkArea(self, number_region):
    from database import Share, Region
    import datetime
    self.sum = 0
    self.shares = session.query(Share.share).filter(Share.region_id == Region.region_id).\
    filter(Region.number_region == self.number_region).all()
    try:
      for self.i in range(len(self.shares)):
        try:
          self.sum = self.sum +self.shares[self.i][0]
        except IndexError:
          self.sum = 0
      self.area = session.query(Region.area).\
      filter(Region.number_region == self.number_region).all()
      
      self.value = self.area[0][0] - self.sum
      if self.value <0:
        self.err = "Please, check area and correct your mistakes"

    except IndexError:
      self.value = None
    return self.value

  def InsertShare(self, login, share, number_region, doc):
    from database import User, Share, isNone
    self.login = login
    self.share = share
    self.number_region = int(number_region)
    self.doc = doc
    self.user_id = session.query(User.id).filter(User.login == self.login).all()
    try:
      self.find = session.query(Share.region_id).filter(Share.user_id == self.user_id[0][0]).filter(Region.number_region == self.number_region).all()
    except:
      self.err = "Такого пользователя не существует!!!"
      return self.err
    if isNone(self.checkArea(self.number_region)) or self.checkArea == 0:
      self.err = "Данный регион либо не существует, либо полностью распределен!!!!!"
      return self.err
    if self.checkArea(self.number_region)-self.share < 0:
      self.err = "Регион переполнен, введите меньшее кол-во"
      return self.err
    print(self.find)
    self.y = []
    for self.i in range(len(self.find)):
      self.y.append(self.find[self.i][0])
    if self.number_region in self.y:
      self.InsertHistory(user_id =self.user_id[0][0], number = self.number_region, share = self.share, id_seller = self.id)
      session.query(Share).filter(Share.user_id == self.user_id[0][0]).update({
                                                            "share": self.share,
                                                            "doc":self.doc})
      session.commit()
      return 0
    else:
      self.region = session.query(Region.region_id).filter(Region.number_region == self.number_region).all()
      self.InsertHistory(user_id =self.user_id[0][0], number = self.number_region, share = self.share, id_seller = self.id)
      self.b = Share(
                    user_id = self.user_id[0][0],
                    region_id = self.region[0][0],
                    share = self.share,
                    doc = self.doc)
      
      return self.b


  def InsertHistory(self, **kwargs):
    from database import HistoryRegion, isNone, Region
    import datetime
    self.kwargs = kwargs
    self.region = session.query(Region.region_id).filter(Region.number_region == self.kwargs.get("number")).all()
    self.row = session.query(HistoryRegion.id_transaction).filter(HistoryRegion.id_transaction >= 0).all()
    try:
      self.id_trans = self.row[len(self.row)-1][0]
    except:
      self.id_trans = None
    if isNone(self.id_trans):
      self.id_transaction = -1
    else:
      self.id_transaction = self.id_trans
    try:
      self.region_id = self.region[0][0]
    except IndexError:
      self.region_id = -1


    self.b = HistoryRegion(     id_transaction = self.id_transaction +1,
                                date = datetime.datetime.now(),
                                region_id = self.region_id,
                                id_buyer = self.kwargs.get("user_id"),
                                share = self.kwargs.get("share"),
                                id_seller = int(self.kwargs.get("id_seller"))
                                  )
    return session.add(self.b)

class ShowHistory:
  def __init__(self, *args):
    self.args = args
  def show_all(self):
    from database import User, Region, HistoryRegion
    self.b = session.query(
    HistoryRegion.date,
    Region.number_region,
    User.NFC,
    HistoryRegion.share).filter(Region.region_id == HistoryRegion.region_id).all()
    return self.b

  def show_area(self, date):
    from database import User, Region, HistoryRegion
    self.date = date
    return session.query(
    HistoryRegion.date,
    Region.number_region,
    User.NFC,
    HistoryRegion.share).filter(Region.region_id == HistoryRegion.region_id).\
                          filter(HistoryRegion.date > self.date[0]).\
                          filter(HistoryRegion.date < self.date[1]).all()



class ShowDirectorAPI(ShowHistory, ShowData, Companies, Inventories, Debts):
  def __init__(self, **kwargs):
    self.kwargs = kwargs
    super(ShowDirectorAPI, self).__init__()


  def showHist(self, *args):
    self.args = args
    try:
      self.value = ShowHistory().show_area(self.args)
    except IndexError:
      self.value = ShowHistory().show_all()
    return self.value
  
  def showData(self, **kwargs):
    self.kwargs = kwargs
    self.value = ShowData().get_table_history_payment(full_name = self.kwargs.get("full_name"), number_region = self.kwargs.get("number_region"))
    return self.value
  
  def showComp(self, *args):
    self.args = args
    if len(self.args) != 0:
      self.value = Companies().show_area(self.args)
    else:
      self.value = Companies().show_all()
    return self.value
  
  def showInvent(self):
    
    self.value = Inventories().show_all()
    return self.value
  def showDebt(self):
    
    self.value = Debts().show_all()
    return self.value



class InsertDirectorAPI(Share_work, Region_work, NewInventory, NewUser):
  def __init__(self, *args):
    self.args = args
    super().__init__(self.args)

  def insertUser(self, login, password, full_name, membership, privelege):
    self.login = login
    self.password = password
    self.full_name = full_name
    self.membership = membership
    self.privelege = privelege
    return NewUser().createUser(self.login, self.password, self.full_name, self.membership, self.privelege)
  def insertInv(self, name):
    self.name = name
    return NewInventory(self.name).insertInventory(self.name)
  def insertShare(self,ids, login, share, number_region, doc):
    self.id = ids
    self.login = login
    self.share = share
    self.number_region = number_region
    self.doc = doc
    return Share_work(self.id).InsertShare(self.login, self.share, self.number_region, self.doc)
  def insertRegion(self, area):
    self.area = area
    return Region_work().insertRegion(self.area)
  def updateRegion(self, number, area):
    self.number = number
    self.area = area
    return Region_work().updateRegion(self.number, self.area)


de = create_debug_engine(True)
session = create_session(de)



