# 3 ta mahsulot bo'lsin (masalan, Olma â€“ 5000 so'm, Banan â€“ 7000 so'm, Uzum â€“ 8000 so'm). 
# Har biri QCheckBox sifatida yozilsin. Foydalanuvchi tanlagan mahsulotlarning umumiy narxi oynaning pastida
# QLabel da chiqib tursin.

import os
os.system("cls")

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout)

check_style = """
    font-size: 30px;
    color: black;
    """

app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Market")
        self.setGeometry(1350, 200, 500, 600)
        self.setStyleSheet("background-color: #8f8ca3")
        self.vbox = QVBoxLayout()

        self.check1 = QCheckBox("Olma - 5000")
        self.check1.setStyleSheet(check_style)
        self.vbox.addWidget(self.check1)
        self.check1.stateChanged.connect(self.checkbox_func)

        self.check2 = QCheckBox("Banan - 7000")
        self.check2.setStyleSheet(check_style)
        self.vbox.addWidget(self.check2)
        self.check2.stateChanged.connect(self.checkbox_func)

        self.check3 = QCheckBox("Uzum - 8000")
        self.check3.setStyleSheet(check_style)
        self.check3.stateChanged.connect(self.checkbox_func)
        self.vbox.addWidget(self.check3)
        
        self.label = QLabel("Umumiy narx: ")
        self.label.setStyleSheet(check_style)
        self.vbox.addWidget(self.label)

        self.setLayout(self.vbox)

        

    def checkbox_func(self):
        res = 0 
        if self.check1.isChecked():
            res += 5000
        if self.check2.isChecked():
            res += 7000
        if self.check3.isChecked():
            res += 8000
        self.label.setText(f"Umumiy narx: {res} sum")

win = Window()
win.show()
app.exec_()