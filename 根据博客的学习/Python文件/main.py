import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

from 根据博客的学习.Python文件 import 汇率转换器
from functools import partial
def click_success():
    print("HelloWorld")

def convert(ui):
    input=ui.lineEdit.text()
    result=float(input)*6.7
    ui.lineEdit_2.setText(str(result))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=汇率转换器.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(convert,ui))
    sys.exit(app.exec_())


