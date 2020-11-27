import sys
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication, QHBoxLayout, QWidget,QPushButton  # QHBoxLayout水平布局
from PyQt5.QtGui import QIcon

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        #添加Button
        self.button1=QPushButton('退出应用程序')
        #将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)

        #定义一个水平布局
        layout=QHBoxLayout()
        layout.addWidget(self.button1)
        #将所有的组件都放到QWidget
        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        #将QWidget放到主屏幕上
        self.setCentralWidget(mainFrame)

    #按钮的单击事件的方法(自定义的槽)
    def onClick_Button(self):
        sender=self.sender()
        print(sender.text()+'按钮被按下')
        app=QApplication.instance()
        app.quit()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QuitApplication()
    main.show()
    sys.exit(app.exec_())
