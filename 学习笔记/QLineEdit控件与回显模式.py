'''
QLineEdit控件与回显模式
基本功能：输入单行的文本
EchoMode设置回显模式
1.Normal 输入显示
2.NoEcho 输入不显示
3.Password 输入密码
3.PasswordEchoOnEdit 编辑时可看，之后不可看
'''

from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLineEdit控件与回显模式')
        formLayout=QFormLayout()

        normalLineEdit=QLineEdit()
        noEchoLineEdit=QLineEdit()
        passwordLineEdit=QLineEdit()
        passwordEchoOnEditLineEdit=QLineEdit()

        formLayout.addRow("Normal",normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password",passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit",passwordEchoOnEditLineEdit)

        #placeholdertext

        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        #应用表单布局
        self.setLayout(formLayout)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())

