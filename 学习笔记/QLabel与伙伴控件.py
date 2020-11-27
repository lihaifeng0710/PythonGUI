'''
QLabel与伙伴控件
mianLayout.addWidget(控件伙伴，rowIndex，columnIndex,row,column)rowIndex，columnIndex控件的位置||||||row,column控件的尺寸
'''
from PyQt5.QtWidgets import *
import sys
class QLabelBuddy(QDialog):
    #对话框的基类
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        nameLabel=QLabel('&Name',self)
        nameLineEdit=QLineEdit(self)
        #设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        PasswordLabel = QLabel('&Password', self)
        PasswordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        PasswordLabel.setBuddy(PasswordLineEdit)

        btnOK=QPushButton('&OK')
        btnCancel=QPushButton('&Cancel')


        mainLayout=QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)
        mainLayout.addWidget(PasswordLabel,1,0)
        mainLayout.addWidget(PasswordLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)

if __name__=='__main__':
    app=QApplication(sys.argv)

    main=QLabelBuddy()
    main.show()
    sys.exit(app.exec_())



