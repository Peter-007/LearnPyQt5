import sys
from math import *
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import *

class Form(QWidget):

    def __init__(self):
        super().__init__()
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()

        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            due = QTime.currentTime()
            text = self.lineedit.text()
            self.browser.append("{} => {} = <b>{}</b>".format(due.toString(),text,
                                eval(text)))
        except:
            self.browser.append("<font color=red>{} is invalid!</font>"
                                .format(text))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
