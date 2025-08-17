#konsola pyuic5 ****.ui -o dosyaadi.py

from PyQt5 import QtWidgets
import sys
import os
from MainWindow import Ui_MainWindow

qt_plugins_path = os.path.join(os.path.dirname(QtWidgets.__file__), 'Qt5/plugins')
os.environ['QT_PLUGIN_PATH'] = qt_plugins_path

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.hesapla)
        self.ui.btn_ckarma.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla)


    def hesapla(self):
        sender = self.sender().text()
        print(sender)
        result = 0
        if sender == "Toplama":
            result = int(self.ui.txtsayi1.text()) + int(self.ui.txtsayi2.text())
        elif sender =="Çıkarma":
            result = int(self.ui.txtsayi1.text()) - int(self.ui.txtsayi2.text())
        elif sender =="Çarpma":
            result = int(self.ui.txtsayi1.text()) * int(self.ui.txtsayi2.text())
        elif sender =="Bölme":
            result = int(self.ui.txtsayi1.text()) / int(self.ui.txtsayi2.text())
        else:
            print("buton bulunamadı")
        self.ui.lbl_sonuc.setText(f"Sonuc : {result}")

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()

