'''
'''
from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit控件输入多行文本使用')

        self.resize(300,280)

        self.textEdit=QTextEdit()
        self.buttonText=QPushButton('显示文本')
        self.buttonHTML=QPushButton('显示HTML')

        self.buttonToText = QPushButton('获取文本')
        self.buttonToHTML = QPushButton('获取HTML')


        layout=QVBoxLayout()#垂直布局
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHTML)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)
        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonToHTML.clicked.connect(self.onClick_ButtonToHTML)


    def onClick_ButtonText(self):
        self.textEdit.setPlainText('Hello Word,世界你好吗')

    def onClick_ButtonToText(self):
        print(self.textEdit.toPlainText())

    def onClick_ButtonHTML(self):
        self.textEdit.setHtml('<font color="blue" size="5">Hello world</font>')

    def onClick_ButtonToHTML(self):
        print(self.textEdit.toHtml())


if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QTextEditDemo()
    main.show()
    sys.exit(app.exec_())

