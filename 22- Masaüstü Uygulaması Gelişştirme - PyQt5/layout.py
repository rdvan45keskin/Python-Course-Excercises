import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette,QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)

        hlayout1 = QtWidgets.QHBoxLayout()        # horizon box layout
        hlayout1.addWidget(Color("red"))
        hlayout1.addWidget(Color("blue"))
        hlayout1.addWidget(Color("green"))
        # hlayout1.setContentsMargins(30,20,0,30)
        # hlayout1.setSpacing(50)

        hlayout2 = QtWidgets.QHBoxLayout()        # horizon box layout
        hlayout2.addWidget(Color("red"))
        hlayout2.addWidget(Color("green"))

        vlayout = QtWidgets.QVBoxLayout()         # vertical box layout
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)


        # # --------GRID LAYOUT----------
        # layout = QtWidgets.QGridLayout()
        # layout.addWidget(Color("Red"),0,0)          # 
        # layout.addWidget(Color("blue"),1,0)         # 1 aşağı
        # layout.addWidget(Color("green"),0,2)        # 2 sağa
        # layout.addWidget(Color("yellow"),3,1)       # 3 aşağı 1 sağa


        widget = QWidget()
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()