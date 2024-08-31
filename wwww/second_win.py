from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QLabel

from instr import *
from final_win import *


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # створюємо та налаштовуємо графічні елементи
        self.connects()  # Встановлює зв'язки між елементами
        self.set_appear()  # Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.show()  # старт

    def set_appear(self):
        self.setWindowTitle("Тест Руф'є")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        lbl1 = QLabel(txt_name)
        lbl2 = QLabel(txt_age)
        lbl3 = QLabel(txt_test1)
        lbl4 = QLabel(txt_test2)
        lbl5 = QLabel(txt_test2)
        lbl6 = QLabel()

        self.btn1 = QPushButton(txt_starttest1)
        self.btn2 = QPushButton(txt_starttest2)
        self.btn3 = QPushButton(txt_starttest3)
        self.btn4 = QPushButton(txt_sendresults)

        self.le1 = QLineEdit(txt_hintname)
        self.le2 = QLineEdit()
        self.le3 = QLineEdit()
        self.le4 = QLineEdit()
        self.le5 = QLineEdit()

        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        h_line = QHBoxLayout()

        v1.addWidget(lbl1, alignment=Qt.AlignLeft)
        v1.addWidget(self.le1, alignment=Qt.AlignLeft)
        v1.addWidget(lbl2, alignment=Qt.AlignLeft)
        v1.addWidget(self.le2, alignment=Qt.AlignLeft)
        v1.addWidget(lbl3, alignment=Qt.AlignLeft)
        v1.addWidget(self.btn1, alignment=Qt.AlignLeft)
        v1.addWidget(self.le3, alignment=Qt.AlignLeft)
        v1.addWidget(lbl4, alignment=Qt.AlignLeft)
        v1.addWidget(self.btn2, alignment=Qt.AlignLeft)
        v1.addWidget(lbl5, alignment=Qt.AlignLeft)
        v1.addWidget(self.btn3, alignment=Qt.AlignLeft)
        v1.addWidget(self.le4, alignment=Qt.AlignLeft)
        v1.addWidget(self.le5, alignment=Qt.AlignLeft)
        v1.addWidget(self.btn4, alignment=Qt.AlignCenter)
        v2.addWidget(lbl6)

        h_line.addLayout(v1)
        h_line.addLayout(v2)

        self.setLayout(h_line)

    def next_click(self):
        self.hide()
        self.finalWin = FinalWin()

    def connects(self):
        self.btn4.clicked.connect(self.next_click)
