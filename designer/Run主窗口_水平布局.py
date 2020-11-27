import sys
import 主窗口_水平布局
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=主窗口_水平布局.Ui_MainWindow()
    #向窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    #进入主循环
    sys.exit(app.exec_())

