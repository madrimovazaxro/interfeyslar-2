#  3 ta QRadioButton bo'lsin: Qizil, Yashil, Ko'k. Tanlangan rangga qarab oynaning fon rangi o'zgarib tursin.

import os
os.system("cls")

from PyQt5.QtWidgets import (QApplication, QWidget, QRadioButton, QVBoxLayout)

r_style = """
font-size: 30px;
color: white;
"""

app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Colors")
        self.setStyleSheet("Background-color: #6a606e;")
        self.setGeometry(1350, 200, 500, 600)
        self.vbox = QVBoxLayout()

        self.r1 = QRadioButton("Qizil")
        self.r1.setStyleSheet(r_style)
        self.r1.clicked.connect(self.rad_func)
        self.vbox.addWidget(self.r1)

        self.r2 = QRadioButton("Yashil")
        self.r2.setStyleSheet(r_style)
        self.r2.clicked.connect(self.rad_func)
        self.vbox.addWidget(self.r2)

        self.r3 = QRadioButton("Ko'k")
        self.r3.setStyleSheet(r_style)
        self.r3.clicked.connect(self.rad_func)
        self.vbox.addWidget(self.r3)

        self.setLayout(self.vbox)

    def rad_func(self):
        if self.r1.isChecked():
            self.setStyleSheet("background-color: red;")
        if self.r2.isChecked():
            self.setStyleSheet("background-color: green;")
        if self.r3.isChecked():
            self.setStyleSheet("background-color: blue;")



win = Window()
win.show()
app.exec_()