import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

qt_plugins_path = os.path.join(os.path.dirname(QtWidgets.__file__), 'Qt5/plugins')
os.environ['QT_PLUGIN_PATH'] = qt_plugins_path


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("first application")
    win.setGeometry(200,200,500,500)        # ilk 2 parametre sol üste göre konumu son 2 parametre boyutu belirler
    win.setWindowIcon(QIcon("4070.png"))
    win.setToolTip("my tooltip")


    win.show()
    sys.exit(app.exec_())


window()

