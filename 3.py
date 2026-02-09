# QComboBox ichida "Python", "C++", "Java" variantlari bo'lsin.
# Foydalanuvchi tanlagan til QLabel da chiqsin.

import os
os.system('cls')

from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QLabel, QVBoxLayout)

app = QApplication([])

c_style = """
    background-color: white;
    font-size: 30px;
    color: black;
"""
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Directions")
        self.setGeometry(1550, 300, 500,600 )
        self.setStyleSheet("background-color: #c48210;")
        self.vbox = QVBoxLayout()

        self.set_combo()
        self.setLayout(self.vbox)

        self.label = QLabel("")
        self.label.setStyleSheet("color: white; font-size: 30px;")
        self.vbox.addWidget(self.label)

    

        
    def c_changed(self):
        text = self.c.currentText()
        self.label.setText(f"Tanlangan til: {text}")    

    def set_combo(self):
        self.c = QComboBox()
        self.c.addItems(["Python", "C++", "Java"])
        self.c.setStyleSheet(c_style)
        self.c.currentTextChanged.connect(self.c_changed)
        self.vbox.addWidget(self.c)
    
    

win = Window()
win.show()
app.exec_()