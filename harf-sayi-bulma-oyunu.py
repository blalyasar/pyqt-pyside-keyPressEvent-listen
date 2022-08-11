import sys
import time
import string
import random
import threading
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import *


class Example(QWidget):
    def __init__(self, parent = None):

        lname = list(string.ascii_lowercase)
        #lname = ['alif','beh','teh','theh','jim','ha','kha','dal','dhal','ra','zin','sin','shin','Sad','Dad','Ta','DHa','ain','ghain','feh','qaf','kaf','lam','mim','nün','heh','waw','yeh', 'Sifr', 'wáaHid', 'ithnáyn', 'thaláatha','árba:ah', 'khámsah', 'sittah','sáb:ah', 'thamáanyah', 'tís:ah']
        self.L = list(string.ascii_lowercase + string.digits)
        #L = [u"\u0627", u"\u0628", u"\u062A", u"\u062B", u"\u062C",u"\u062D", u"\u062E", u"\u062F", u"\u0630", u"\u0631", u"\u0632", u"\u0633", u"\u0634", u"\u0635", u"\u0636", u"\u0637", u"\u0638", u"\u0639", u"\u063A", u"\u0641", u"\u0642", u"\u0643", u"\u0644", u"\u0645", u"\u0646", u"\u0647", u"\u0648", u"\u064A", u"\u0660", u"\u0661", u"\u0662", u"\u0663", u"\u0664", u"\u0665", u"\u0666", u"\u0667", u"\u0668", u"\u0669" ]


        super(Example, self).__init__(parent)
        self.initUI()
       
    def initUI(self):

        keyPressed = pyqtSignal(int)

        QToolTip.setFont(QFont('DejaVuSans', 30))
       
        vbox = QHBoxLayout()
        self.lbl2 = QLabel(self)
 
        self.lbl2.setFont(QFont('FreeSerif', 100))
        self.lbl2.setText(str(random.choice(self.L)))
        self.lbl2.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.lbl2)
        self.setLayout(vbox)

        self.setWindowTitle(' ')  
        self.setGeometry(100,100,700,700)

        self.show()

    def keyPressEvent(self, event):
        print("press    ")
        if type(event) ==  QKeyEvent:
            print("EVENT KEY ",event.key()) # sayi veriyor
            print("LABEL TEXT ",self.lbl2.text())
            print("TEXTIN ORD  HALI ", ord(self.lbl2.text()))
            print(type(ord(self.lbl2.text())))
            print(type(event.key()))

            # for letters
            if  isinstance( self.lbl2.text(), str ) :
                if event.key() ==  ord(self.lbl2.text()) -32   :
                    print("TEXT karekter DEGISIYOR")
                    self.lbl2.setText(random.choice(self.L))

            # for numbers
            if event.key() ==  ord(self.lbl2.text()) :
                print("TEXT ınt DEGISIYOR")
                self.lbl2.setText(random.choice(self.L))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
