'''
QMainWindow:
可以包含菜单栏，工具栏，状态栏，标题栏，最常见的窗口形式
QWidget:
不确定窗口的用途，就使用
QDialog:
是对话窗口的基类，没有菜单栏，工具栏，状态栏
'''
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)
        #设置主窗口的标题
        self.setWindowTitle('量子电路模拟实验平台')
       #设置主窗口的尺寸
        self.resize(400,300)
        self.status=self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)

if __name__=='__main__':
    app=QApplication(sys.argv)
    #app.setWindowIcon()
    main=FirstMainWin()
    main.show()
    sys.exit(app.exec_())
