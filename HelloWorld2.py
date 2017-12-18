import sys
from PyQt5.QtWidgets import *

# 从PyQt库导入QtWidget通用窗口类
class Form(QWidget):
    # 自己建一个Form类，以class开头，Form是自己的类名，
    # QWidget 是继承QtWidgets类
    def __init__(self):
        super().__init__()
        # 创建一个标签
        lblMsg = QLabel("<font color=green size=12><b>Hello World</b></font>", self)
        # 设置窗体的位置、大小
        self.setGeometry(500, 200, 200, 50)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # pyqt窗口必须在QApplication方法中使用
    form =Form()    # 创建Form对象
    form.show()     # 显示窗体
    app.exec_()     # 调用app.exec_()会开始执行QApplication对象的事件循环。
