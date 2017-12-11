import sys      # 导入sys模块是需要读取sys.argv列表中的命令行参数信息
import time     # 导入time模块是要使用sleep()函数
from PyQt5.QtCore import *      # 要使用QTime类
from PyQt5.QtWidgets import *   # 要使用图形控件QLabel类

# 每个PyQt GUI应用程序都必须有一个QApplication对象。
# 这个对象提供访问全局信息的能力，如程序目录、屏幕大小等。
# 还会提供事件循环
app = QApplication(sys.argv)

try:
    due = QTime.currentTime()   # 初始化目标时间为当前时间
    message = "Alert!"  # 初始化默认的提示信息

    # 若未给定命令行参数，则抛出此异常，给出一条提示信息说明"用法"
    if len(sys.argv) < 2:
        raise ValueError

    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours), int(mins))

    # 若目标时间参数格式无效，则抛出此异常
    if not due.isValid():
        raise ValueError

    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])

# 抛出异常时的处理，给出"用法"提示
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]"  # 24hr clock

# 把当前时间和目标循环的进行比较，一旦超过了目标时间，循环就停止。
while QTime.currentTime() < due:
    print(due.toString(), QTime.currentTime().toString())
    time.sleep(10)      # 每隔20秒比较一次，等待期间cpu可给其他应用程序使用

# 窗口控件QLabel可处理HTML文本，这里为加黑、红色、大小为72像素
# 在PyQt中任何窗口控件都可以作为顶级窗口，标签／按钮等都可以
label = QLabel("<font color=red size=72><b>{}</b></font>".format(message))

#label.setWindowFlags(Qt.SplashScreen)
label.show()    # 显示标签信息，会触发绘制事件paint

# 启动定时器，等待30秒后触发超时事件，用于执行slot: app.quit，以终止程序。
QTimer.singleShot(30000, app.quit)

# 调用app.exec_()会开始执行QApplication对象的事件循环。
# 第一个事件是绘制事件, 标签会带着指定的信息显示在屏幕上。
# 第二个事件是定时器超时事件，即30秒后调用QApplication.quit()关闭窗口、释放资源、退出程序。
app.exec_()
