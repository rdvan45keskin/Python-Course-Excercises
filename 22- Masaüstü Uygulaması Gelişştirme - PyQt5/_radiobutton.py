from PyQt5 import QtWidgets
import sys
from radiobuttonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True)
        self.ui.radioUniversite.setChecked(True)

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.radioJaponya.toggled.connect(self.onClickedUlke)

        self.ui.radioIlkokul.toggled.connect(self.onClickedEgitim)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioYuksekLsans.toggled.connect(self.onClickedEgitim)

        self.ui.btn_country.clicked.connect(self.getSelectedUlke)
        self.ui.btn_edu.clicked.connect(self.getSelectedEgitim)

    def onClickedUlke(self):
        radioButton = self.sender()
        # if radioButton.isChecked():
        #     print("seçilen Ülke: "+radioButton.text())

    def onClickedEgitim(self):
        radioButton = self.sender()
        # if radioButton.isChecked():
        #     print("seçilen Eğitim: "+radioButton.text())

    def getSelectedUlke(self):
        items = self.ui.groupUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_country.setText("Seçilen Ülke: "+rb.text())

    def getSelectedEgitim(self):
        items = self.ui.groupEgitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_edu.setText("Seçilen Eğitim: "+rb.text())


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())