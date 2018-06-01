from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem



class Director(QMainWindow):


    def get_id(self):
        return self.user_id


    model = property(get_id)


    def __init__(self, user_id):
        self.user_id = user_id
        super(Director, self).__init__()
        self.wind()


    def wind(self):
        from Director.View.Main_window import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = Director_Controller(self)
        # self.controller.vieww()


class Director_Controller:


    def __init__(self, view):
        self.view = view
        self.user_id = view.model
        ui = view.ui
        ui.comboBox.activated.connect(self.line)
        ui.pushButton.pressed.connect(self.button)
        ui.pushButton1.pressed.connect(self.button1)
        ui.action.triggered.connect(self.newuser)
        ui.action_2.triggered.connect(self.inventory)
        ui.action_3.triggered.connect(self.region)
        ui.action_4.triggered.connect(self.share)
        ui.action_5.triggered.connect(self.see)
        ui.action_6.triggered.connect(self.smth)
        self.vieww()


    def line(self):
        self.text = self.view.ui.comboBox.currentText()
        if self.text == "История регионов" or self.text=="Платежи предприятия":
            self.view.ui.widget.show()
            self.view.ui.widget1.hide()
            self.tables(self.text)
        elif self.text=="История платежей":
            self.view.ui.lineEdit1.setText("Введите №региона")
            self.view.ui.lineEdit1_2.setText("Введите имя")
            self.view.ui.widget1.show()
            self.view.ui.widget.hide()
            self.tables(self.text)
        else:
            self.view.ui.widget.hide()
            self.view.ui.widget1.hide()
            self.tables(self.text)
        return self.text


    def parametr(self, text, *args):
        import datetime
        self.text = text
        self.args = args

        from Director.Director import ShowDirectorAPI
        self.api = ShowDirectorAPI()
        if self.text == "История регионов" or self.text == "Платежи предприятия":

            if len(self.args)!=0 and self.args[0]!='':
                
                self.date1 = self.args[0].split(".")
                
                self.date2 = self.args[1].split(".")
                if self.text == "Платежи предприятия":
                    self.c = self.api.showComp(datetime.datetime(int(self.date1[2]), int(self.date1[1]),int(self.date1[0])),
                datetime.datetime(int(self.date2[2]),int(self.date2[0]),int(self.date2[0])))
                else:
                    self.c = self.api.showHist(datetime.datetime(int(self.date1[2]), int(self.date1[1]),int(self.date1[0])),
                    datetime.datetime(int(self.date2[2]),int(self.date2[0]),int(self.date2[0]))) 
                return self.c
            elif self.text == "Платежи предприятия":
                self.c = self.api.showComp()
            else:
                self.c = self.api.showHist()             
            return self.c
        elif self.text == "Должники":
            return self.api.showDebt()
        elif self.text == "История платежей":
            self.data = []
            if len(self.args)!=0:
                
                self.data.append(str(self.args[0]))
                self.data.append(str(self.args[1]))
            else:

                self.data.append("Введите №региона")
                self.data.append("Введите имя")
            if self.data[0]=="Введите №региона" or self.data[1] == "Введите имя":

                return self.api.showData()
            else:

                return self.api.showData(full_name=self.data[1], number_region=self.data[0])

        else:
            return self.api.showInvent()


    def vieww(self):
        self.text ="История платежей"
        self.view.ui.widget1.show()
        self.view.ui.widget.hide()
        self.view.ui.lineEdit1.setText("Введите №региона")
        self.view.ui.lineEdit1_2.setText("Введите имя")

        self.tables(self.text)


    def tables(self, text, *args):
        self.args = args

        self.table = self.view.ui.tableWidget
        self.table.clear()
        self.text = text
        

        from PyQt5.QtWidgets import QTableWidgetItem
        if len(self.args) == 0:

            self.b= self.parametr(self.text)
        else:

            self.b= self.parametr(self.text, self.args[0], self.args[1])


        self.row = 20
        self.cols = 10
        if self.text == "История платежей":
            self.name = ["ФИО","Дата платежа","Наименование","Цена за единицу","Цена","платеж","переплата","Итог"]
        elif self.text =="Должники":
            self.name = ["ФИО","Наименование","Задолженность"]
        elif self.text == "Инвентарь":
            self.name = ["Дата", "Инвентарный номер", "Наименование", "Наличие"]
        elif self.text =="История регионов":
            self.name = ["Дата покупки", "Номер участка", "ФИО покупателя", "занимаемая площадь"]
        else:
            self.name = ["Дата","ФИО","Наименование услуги","Цена"]



        if len(self.b) ==0:
            self.table.setColumnCount(self.cols)
            self.table.setRowCount(self.row)
            return 0
        else:
            if self.cols >= len(self.b):
                self.table.setColumnCount(self.cols)
            else:
                self.table.setColumnCount(len(self.b))
            if self.row >= len(self.b[0]):
                self.table.setRowCount(self.row)
            else:
                self.table.setRowCount(len(self.b[0]))
        for i in range(len(self.name)):
            self.table.setHorizontalHeaderItem(i,QTableWidgetItem(str(self.name[i])))
        for i in range(len(self.b)):
            
            for j in range(len(self.b[i])):
                
                self.table.setItem(i , j, QTableWidgetItem(str(self.b[i][j])))
        self.table.resizeColumnsToContents()


    def button(self):
        self.a = ""
        self.b = ""
        self.table = self.view.ui.tableWidget
        self.table.clear()
        self.a=self.view.ui.lineEdit.text()
        self.b=self.view.ui.lineEdit_2.text()
        self.text = self.line()
        self.tables(self.text, self.a, self.b)


    def button1(self):
        
        self.table = self.view.ui.tableWidget
        self.u=self.view.ui.lineEdit1.text()
        self.e=self.view.ui.lineEdit1_2.text()
        self.text = self.line()
        self.view.ui.tableWidget.clear()
        self.tables(self.text, self.u, self.e)


    def newuser(self):
        from Director.NewUser import NewUser 
        self.dialog = NewUser()
        self.dialog.show()


    def inventory(self):
        from Director.Inventory import Inventory 
        self.dialog = Inventory()
        self.dialog.show()


    def share(self):
        from Director.Share import Share 
        self.dialog = Share(self.user_id)
        self.dialog.show()


    def region(self):
        from Director.Region import Region 
        self.dialog = Region()
        self.dialog.show()


    def smth(self):
        self.g = Gardener("-11")
        self.g.show()


    def see(self):
        self.g = Gardener(self.user_id)
        self.g.show()