from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QPushButton, QGroupBox ,QWidget, QGridLayout, QLabel, QMessageBox
import time
import sys
import random

SIZE = 4 # 2, 4, 6, 8, 10

class MyWindow(QMainWindow):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle("Card Match")

        self.matches = 0
        self.initUI()
    
    def initUI(self):
        self.matches_label = QLabel(self)
        self.matches_label.setText('Matches: 0')
        self.matches_label.move(10,0)
        button_window = QWidget(self)
        grid = QGridLayout()
        button_window.setLayout(grid)
        button_window.resize(600,600)
        self.sending_button = None
        
        nums = list(range(int((self.size ** 2) / 2))) * 2
        # can optimize shuffle function
        random.shuffle(nums)
        
        positions = [(i, j) for i in range(self.size) for j in range(self.size)]
        for pos, num in zip(positions, nums):
            button = QPushButton(str(num))
            button.setStyleSheet('color: rgba(0,0,0,0)')
            button.clicked.connect(self.clicked)
            grid.addWidget(button, *pos) # (*) unpack operator, same as: position[0], position[1]

    def clicked(self):
        # win
        if (self.matches == (self.size ** 2) / 2):
            self.show_popup('You win!')
        if (self.sending_button == None):
            self.sending_button = self.sender()
            self.sending_button.setStyleSheet('color: rgba(0,0,0,255)')
            self.sending_button.setEnabled(False)
        # made match
        elif (self.match(self.sending_button, self.sender())):
            self.sender().setStyleSheet('color: rgba(0,0,0,255)')
            self.sender().setFlat(False)
            self.sending_button.setEnabled(False)
            self.sender().setEnabled(False)
            self.sending_button = None
            self.matches += 1
            self.matches_label.setText('Matches: ' + str(self.matches))
        # match failed
        else:
            self.sending_button.setEnabled(True)
            self.sender().setStyleSheet('color: rgba(0,0,0,255)')
            QtWidgets.qApp.processEvents()
            time.sleep(.75)
            self.sender().setStyleSheet('color: rgba(0,0,0,0)')
            self.sending_button.setStyleSheet('color: rgba(0,0,0,0)')
            self.sending_button = None

    def match(self, button1, button2):
        if (button1.text() == button2.text()):
            return True
        else:
            return False
    
    def show_popup(self, msg):
        pop = QMessageBox()
        pop.setWindowTitle('Alert')
        pop.setText(msg)
        #pop.setIcon(QMessageBox.warning)
        x = pop.exec_()

def window():
    app = QApplication(sys.argv)
    win = MyWindow(SIZE)
    win.show()
    sys.exit(app.exec_())

window()
