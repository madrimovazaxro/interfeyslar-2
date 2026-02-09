# QLineEdit va yonida Qo'shish tugmasi bo'lsin. Foydalanuvchi QLineEdit ga so'z kiritib tugmani 
# bossa, bu so'z QComboBox ga qo'shilsin.

import os
os.system('cls')

from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, QComboBox, QHBoxLayout, QVBoxLayout)

app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WORDS")
        self.setStyleSheet("background-color: #110863;")
        self.setGeometry(1350, 200, 500, 600)
        self.vbox = QVBoxLayout()
        
        self.hbox = QHBoxLayout()
        self.inpt = QLineEdit()
        self.inpt.setPlaceholderText("Enter the word...")
        self.inpt.setStyleSheet("background-color: white; font-size: 35px; color: black;")
        self.inpt.setGeometry(50, 200, 200, 50)
        self.hbox.addWidget(self.inpt)

        self.btn = QPushButton("+")
        self.btn.setStyleSheet("background-color: white; font-size: 30px; color: black;")
        self.btn.clicked.connect(self.btn_func)
        self.hbox.addWidget(self.btn)

        self.vbox.addLayout(self.hbox)

        self.combo = QComboBox()
        self.combo.setStyleSheet("background-color: white; font-size:30px; color:black;")
        self.vbox.addWidget(self.combo)

        
        self.setLayout(self.vbox)

    def btn_func(self):
        word = self.inpt.text()
        self.combo.addItem(word)
        self.inpt.clear()
 


win = Window()
win.show()
app.exec_()
