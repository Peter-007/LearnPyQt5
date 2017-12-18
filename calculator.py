'''
一个计算器
该示例是一个对话框应用程序，即没有菜单栏、工具条、状态栏。
软件功能：
1.用户输入数学表达式，按回车键后，表达式及结果就会显示出来。
2.如果输入的表达式无效，软件会显示错误信息。
'''

import sys
from math import *  # 输入的表达式可使用math模块中所有数学函数，如sin、cos
from PyQt5.QtWidgets import *   # 使用此模块中的QWidget，QTextBrowser、QLineEdit

# 通过QDialog子类化的方法创建一个顶级窗口
# PyQt中的所有控件都是继承自QWidget, 如：QDialog,QLineEdit
class Form(QDialog):

    def __init__(self):
        super().__init__()   # 初始化窗口

        # 创建两个窗口控件
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()

        # 创建一个垂直布局管理器QVBoxLayout
        # PyQt提供了三种布局管理器：垂直布局／水平布局／网格布局，它们可以彼此嵌套。
        # 使用了布局管理器后，各种控件会随着窗口的大小改变自动调整。
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

        self.lineedit.setFocus()

        # 信号（returnPressed）连接到槽（updateUi)
        # 当用户在lineedit上按下回车键时，retrunPressed信号就会发射出来，
        # 因有connect , 此时会调用updateUi().
        self.lineedit.returnPressed.connect(self.updateUi)

        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineedit.text()

            # 使用eval函数计算表达式的值
            self.browser.append("{} = <b>{}</b>".format(text,eval(text)))
        except:
            self.browser.append("<font color=red>{} is invalid!</font>".format(text))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()   # 创建Form实例
    form.show()
    app.exec_()     # 调用了show()后，事件循环开始，显示出窗口
