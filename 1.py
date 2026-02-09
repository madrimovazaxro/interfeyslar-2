# Dastur oynasida QVBoxLayout yordamida 3 ta tugma (QPushButton) joylashtiring. 
# Har bir tugmani bosganda terminalda bosilgan tugma nomi chiqsin.

import os
os.system('cls')

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout)

app = QApplication([])

btn_style = """
    background-color: white;
    color: black;
    font-size: 20px;
"""

class Window(QWidget):

    def btn1_func(self):
            print(self.btn1.text())
    def btn2_func(self):
            print(self.btn2.text())
    def btn3_func(self):
            print(self.btn3.text())

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons")
        self.setStyleSheet("background-color: blue;")
        self.vbox = QVBoxLayout()

        self.btn1 = QPushButton("Tugma 1")
        self.btn1.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn1)
        self.btn1.clicked.connect(self.btn1_func)

        def btn2_func(self):
            print(self.btn2)
        self.btn2 = QPushButton("Tugma 2")  
        self.btn2.setStyleSheet(btn_style)  
        self.vbox.addWidget(self.btn2)
        self.btn2.clicked.connect(self.btn2_func)

        def btn3_func(self):
            print(self.btn3)
        self.btn3 = QPushButton("Tugma 3")    
        self.btn3.setStyleSheet(btn_style)
        self.vbox.addWidget(self.btn3)
        self.btn3.clicked.connect(self.btn3_func)

        def __str__(self):
            return self.objectName()

        self.setLayout(self.vbox)

        



win = Window()
win.show()
app.exec_()