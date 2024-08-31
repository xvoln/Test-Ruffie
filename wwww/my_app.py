from second_win import *
from instr import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class MainWin(QWidget):
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
        lbl1 = QLabel(txt_hello)
        lbl2 = QLabel(txt_instruction)
        self.btn = QPushButton(txt_next)

        line = QVBoxLayout()
        line.addWidget(lbl1)
        line.addWidget(lbl2)
        line.addWidget(self.btn, alignment=Qt.AlignCenter)

        self.setLayout(line)

    def connects(self):
        self.btn.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.testWin = TestWin()


app = QApplication([])
mw = MainWin()
app.exec_()
