from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
import sys
from _listForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load Students
        self.loadStudents()

        # add new student
        self.ui.btnAdd.clicked.connect(self.addStudent)

        # edit Student
        self.ui.btnEdit.clicked.connect(self.editStudent)

        # delete Student
        self.ui.btnRemove.clicked.connect(self.removeStudent)

        # up
        self.ui.btnUp.clicked.connect(self.upStudent)

        # up
        self.ui.btnDown.clicked.connect(self.downStudent)

        # sort
        self.ui.btnSort.clicked.connect(self.sortStudent)

        # exit
        self.ui.btnExit.clicked.connect(self.close)

    def loadStudents(self):
        liste = ["Ahmet","Ali","Çınar"]
        self.ui.listItems.addItems(liste)
        self.ui.listItems.setCurrentRow(0)

    def addStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        text ,ok = QInputDialog.getText(self,"New Student","Student Name")
        if ok and text is not None:
            self.ui.listItems.insertItem(currentIndex,text)

    def editStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is not None:
            text,ok = QInputDialog.getText(self, "Edit Student", "Student Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)
    
    def removeStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is None:
            return
        
        question = QMessageBox.question(self, "Remove Student", "Are you Sure? "+item.text(), QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(index)
            del item

    def upStudent(self):
        index = self.ui.listItems.currentRow()
        if index >= 1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1, item)
            self.ui.listItems.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.listItems.currentRow()
        if index < self.ui.listItems.count() - 1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1, item)
            self.ui.listItems.setCurrentItem(item)

    def sortStudent(self):
        self.ui.listItems.sortItems()

    def close(self):
        quit()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()