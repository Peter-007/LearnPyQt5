import sys
from PyQt5.QtWidgets import *

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.lblMsg = QLabel("2018/1/18")
        self.fromComboBox = QComboBox()
        self.fromSpinBox = QSpinBox()
        self.edt = QLineEdit()

        grid = QGridLayout()
        grid.addWidget(self.lblMsg,0,0)
        grid.addWidget(self.fromComboBox,1,0)
        grid.addWidget(self.fromSpinBox,2,0)
        grid.addWidget(self.edt,3,0)
        self.setLayout(grid)

        self.fromComboBox.addItems(['a','b'])
        self.fromSpinBox.valueChanged.connect(self.updateUi)
        self.fromComboBox.currentIndexChanged.connect(self.updateUi)

    def updateUi(self):
        print("call updateUI")
        #self.edt.setText(str(self.fromSpinBox.value()))

app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec_())
