from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from instr import *


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # створюємо та налаштовуємо графічні елементи
        self.set_appear()  # Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.show()  # старт

    def set_appear(self):
        self.setWindowTitle("Тест Руф'є")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        lbl1 = QLabel(txt_index)
        lbl2 = QLabel(txt_workheart)

        line = QVBoxLayout()
        line.addWidget(lbl1, alignment=Qt.AlignCenter)
        line.addWidget(lbl2, alignment=Qt.AlignCenter)

        self.setLayout(line)
