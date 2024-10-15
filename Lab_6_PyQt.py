from PyQt6.QtWidgets import *
import random


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 300)
        self.setWindowTitle('Генератор случайных чисел')

        self.label = QLabel()
        button = QPushButton('Нажми меня')

        main_l = QVBoxLayout()

        main_l.addStretch()
        main_l.addWidget(self.label)
        main_l.addWidget(button)
        main_l.addStretch()

        self.setLayout(main_l)

        button.clicked.connect(self.press)

    def press(self):
        self.label.setText(f'Случайное чиcло: {random.randint(1, 100)}')


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
