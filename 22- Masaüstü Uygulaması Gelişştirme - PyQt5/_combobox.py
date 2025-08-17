from PyQt5 import QtWidgets
import sys
from comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # combo = self.ui.cbSehirler

        # combo.addItem("Istanbul")
        # combo.addItem("Ankara")
        # combo.addItem("Izmir ")
        # combo.addItem("Antalya")
        # combo.addItems(["Istanbul","Ankara","Izmir","Antalya","Manisa"])

        self.ui.lblLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItems)
        self.ui.btnClear.clicked.connect(self.ClearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.selectedChangedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.selectedChangedText)

    def LoadItems(self):
        sehirler = ["Istanbul","Ankara","Izmir","Antalya","Manisa"]
        self.ui.cbSehirler.addItems(sehirler)

    def GetItems(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())

        count = self.ui.cbSehirler.count()
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))

    def ClearItems(self):
        self.ui.cbSehirler.clear()

    def selectedChangedIndex(self,Index):
        print(Index)

    def selectedChangedText(self,text):
        print(text)
    

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()