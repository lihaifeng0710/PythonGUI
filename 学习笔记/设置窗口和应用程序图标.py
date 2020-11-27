'''
窗口的setWindowIcon方法用于设置窗口的图标，只在windows中可用
QApplication中的setWindowIcon方法只能用于设置主窗口的图标和应用程序图标，但调用了窗口的setWindowIcon方法
'''
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
class IconForm(QMainWindow):
    def __init__(self,parent=None):
        super(IconForm,self).__init__(parent)
        self.initUI()

    def initUI(self):
        #使用坐标系
        self.setGeometry(300,300,250,250)
        #设置主窗口的标题
        self.setWindowTitle('量子电路模拟实验平台')
        #设置窗口图标
        #self.setWindowIcon()


if __name__=='__main__':
    app=QApplication(sys.argv)
    #app.setWindowIcon()
    main=IconForm()
    main.show()
    sys.exit(app.exec_())
