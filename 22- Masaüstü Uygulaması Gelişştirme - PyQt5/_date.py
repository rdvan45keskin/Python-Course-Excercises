from PyQt5 import QtWidgets
import sys
from _dateForm import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.Calculate)

    def Calculate(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateEnd.date()
        print(start,end)

        print(f"Days in month: {start.daysInMonth()}")
        print(f"Days in year: {start.daysInYear()}")

        print(f"total days: {start.daysTo(end)}")

        now = QDate.currentDate()

        print(f"total days from now: {start.daysTo(now)}")


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()