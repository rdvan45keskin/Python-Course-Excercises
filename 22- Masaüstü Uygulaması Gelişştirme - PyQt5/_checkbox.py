import sys
from PyQt5 import QtWidgets
from _cbConverted import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # hobiler
        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbOyun.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)
        self.ui.btnHChoose.clicked.connect(self.get_all_checkedH)

        # dersler
        self.ui.cbWebTasarim.stateChanged.connect(self.show_state)
        self.ui.cbProgramlama.stateChanged.connect(self.show_state)
        self.ui.cbVeriTabani.stateChanged.connect(self.show_state)
        self.ui.btnDChoose.clicked.connect(self.get_all_checkedD)

    def show_state(self,value):
        cb = self.sender()
        # print(cb.text())
        # print(cb.isChecked())

    #hobilerde seçilen checkboxları alma
    def get_all_checkedH(self):
        result = ""
        items = self.ui.GroupHobiler.findChildren(QtWidgets.QCheckBox)
        for i in items:
            if i.isChecked():
                result += i.text() + "\n"
        self.ui.lblHResult.setText(result)

    #derslerde seçilen checkboxları al
    def get_all_checkedD(self):
        result = ""
        items = self.ui.GroupDersler.findChildren(QtWidgets.QCheckBox)
        for i in items:
            if i.isChecked():
                result += i.text() + "\n"
        self.ui.lblDResult.setText(result)

    



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()

    