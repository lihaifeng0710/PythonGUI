'''
屏幕坐标系
原点位于左上角
'''


def onClick_Button():
    print("1")
    print("widget.x()=%d"%widget.x())
    print("widget.y()=%d" % widget.y())
    print("widget.width()=%d" % widget.width())
    print("widget.height()=%d" % widget.height())

    print("2----通过坐标系")
    print("widget.x()=%d"%widget.geometry().x())
    print("widget.y()=%d" % widget.geometry().y())
    print("widget.width()=%d" % widget.geometry().width())
    print("widget.height()=%d" % widget.geometry().height())

    print("3----通过框架")
    print("widget.frameGeometry().x()=%d" % widget.frameGeometry().x())
    print("widget.y()=%d" % widget.frameGeometry().y())
    print("widget.width()=%d" % widget.frameGeometry().width())
    print("widget.height()=%d" % widget.frameGeometry().height())


import sys
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication, QHBoxLayout, QWidget,QPushButton
app=QApplication(sys.argv)

widget=QWidget()
bth=QPushButton(widget)
bth.setText("按钮")
bth.clicked.connect(onClick_Button)

bth.move(24,52)
widget.move(250,200)
widget.resize(300,240)  #设置工作区的尺寸
widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec_())

