import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

qt_plugins_path = os.path.join(os.path.dirname(QtWidgets.__file__), 'Qt5/plugins')
os.environ['QT_PLUGIN_PATH'] = qt_plugins_path

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setWindowTitle("calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):                                 #--------Arayüz kodları------
        self.lbl_sayi1 = QtWidgets.QLabel(self)             # yazı
        self.lbl_sayi1.setText("Sayi 1: ")
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)          # input
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayi 2: ")
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)          # input
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesapla)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çıkar")
        self.btn_cikar.move(150,170)
        self.btn_cikar.clicked.connect(self.hesapla)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText("Çarp")
        self.btn_carp.move(150,210)
        self.btn_carp.clicked.connect(self.hesapla)

        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText("Böl")
        self.btn_bol.move(150,250)
        self.btn_bol.clicked.connect(self.hesapla)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("Sonuc : ")
        self.lbl_sonuc.move(150,290)

    def hesapla(self):
        sender = self.sender().text()
        print(sender)
        result = 0
        if sender == "Topla":
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender =="Çıkar":
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender =="Çarp":
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender =="Böl":
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        else:
            print("buton bulunamadı")
        self.lbl_sonuc.setText(f"Sonuc : {result}")











def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()