#python -m PyQt5.uic.pyuic -x num_pad.ui -o num_pad.py
# pyrcc5 img.qrc -o img.py


from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from pass_sc import Ui_Form as Pass_sc
from PyQt5.QtCore import pyqtSignal
from num_pad import Ui_Form as np

class Ekran1(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.app1 = Pass_sc()
        self.app1.setupUi(self)
        self.pw = 1234
        self.app1.digit_pass.clicked.connect(self.kec)
        self.app1.ok.clicked.connect(self.ok)
    
    def ok(self):
        self.cur = self.app1.password_lineedit.text()
        if str(self.cur) == str(self.pw):
            QMessageBox.information(None, "Succesfull", "Correct Password.")
        else:
            
            QMessageBox.warning(None, "Error", "Uncorrect Password.")

    
    def sil(self):
        self.cur = self.app1.password_lineedit.text()
        self.app1.password_lineedit.setText(self.cur[:len(self.cur)-1])
    
    def kec(self):
        self.kec = Ekran2()
        self.kec.number_data.connect(self.change)
        self.kec.sil.connect(self.sil)
        self.kec.show()
    def change(self,d):
        self.cur = self.app1.password_lineedit.text()
        self.app1.password_lineedit.setText(str(self.cur)+str(d)) 
        
        
  
class Ekran2(QWidget):
    sil = pyqtSignal()
    number_data = pyqtSignal(str)
    def __init__(self) -> None:
        super().__init__()
        self.app2 = np()
        self.app2.setupUi(self)
        self.app2.bir.clicked.connect(lambda x: self.number_f('1'))
        self.app2.iki.clicked.connect(lambda x: self.number_f('2'))
        self.app2.uc.clicked.connect(lambda x: self.number_f('3'))
        self.app2.dord.clicked.connect(lambda x: self.number_f('4'))
        self.app2.bes.clicked.connect(lambda x: self.number_f('5'))
        self.app2.alti.clicked.connect(lambda x: self.number_f('6'))
        self.app2.yeddi.clicked.connect(lambda x: self.number_f('7'))
        self.app2.sekkiz.clicked.connect(lambda x: self.number_f('8'))
        self.app2.doqquz.clicked.connect(lambda x: self.number_f('9'))
        self.app2.sifir.clicked.connect(lambda x: self.number_f('0'))
        self.app2.sil.clicked.connect(self.sil_f)
        self.app2.ok.clicked.connect(lambda: self.close())


   
    
    def number_f(self,data):
        self.number_data.emit(data)
    def sil_f(self):
        self.sil.emit()

app = QApplication([])
ekran = Ekran1()
ekran.show()
app.exec_()
