import sys
from PyQt5.QtWidgets import *

# pyqt窗口必须在QApplication方法中使用
app = QApplication(sys.argv)

# qt支持html标签，强大吧
label = QLabel("<font color=green size=12><b>Hello World</b></font>")

# 有了实例，就需要用show()让他显示
label.show()

# 消息结束的时候，进程结束，并返回0，接着调用sys.exit(0)退出程序
sys.exit(app.exec_())
