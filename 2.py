# QHBoxLayout ichida "Chapga", "O'rtaga", "O'ngga" tugmalarini joylashtiring. 
# Bosilganda QLabel oynada tegishli matnni ko'rsatsin.

import os
os.system('cls')

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QHBoxLayout)

btn_style = """
    background-color: white;
    color: black;
    font-size: 20px;
"""
app = QApplication([])

class Window(QWidget):
    
    def btn1_func(self):
       self.label.setText((self.btn1).text())
    def btn2_func(self):
       self.label.setText((self.btn2).text())
    def btn3_func(self):
       self.label.setText((self.btn3).text())

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Directions")
        self.setStyleSheet("background-color: #38523f;")
        self.vbox = QHBoxLayout()

        self.label = QLabel("Tanlang->")
        self.label.setStyleSheet("color: white; font-size: 30px;")
        self.vbox.addWidget(self.label)
    
        self.btn1 = QPushButton("Chapga")
        self.btn1.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn1)
        self.btn1.clicked.connect(self.btn1_func)

        self.btn2 = QPushButton("O'rtaga")
        self.btn2.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn2)
        self.btn2.clicked.connect(self.btn2_func)
        
        self.btn3 = QPushButton("O'ngga")
        self.btn3.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn3)
        self.btn3.clicked.connect(self.btn3_func)

        self.setLayout(self.vbox)

win = Window()
win.show()
app.exec_()