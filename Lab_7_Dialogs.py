from PyQt6.QtWidgets import *
import random


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 300)
        self.setWindowTitle('Угадай число')

        self.random_number = random.randint(1, 100)
        self.numb_line = QLineEdit()
        self.numb_line.setPlaceholderText('Введите число')
        button = QPushButton('Проверить')
        ext_button = QPushButton('Выход')

        main_l = QVBoxLayout()

        main_l.addStretch()
        main_l.addWidget(self.numb_line)
        main_l.addWidget(button)
        main_l.addWidget(ext_button)
        main_l.addStretch()

        self.setLayout(main_l)

        button.clicked.connect(self.answer)
        ext_button.clicked.connect(self.exit)

    def answer(self):
        message = QMessageBox()
        message.setWindowTitle('Ответ')
        if int(self.numb_line.text()) == self.random_number:
            message.setText('Отгадал!')
        elif int(self.numb_line.text()) > self.random_number:
            message.setText('Загаданное число меньше!')
        else:
            message.setText('Загаданное число больше!')
        message.exec()

    def exit(self, event):
        QApplication.quit()


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
