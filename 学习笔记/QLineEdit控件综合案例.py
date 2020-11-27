from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        x=1

if __name__=='__main__':
    app=QApplication(sys.argv)

    main=QLineEditDemo()
    main.show()
    sys.exit(app.exec_())
