from PyQt6.QtWidgets import *
from collections import Counter


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(600, 400)
        self.setWindowTitle('Текстовый редактор')

        self.input_file = QLineEdit()
        new_file_button = QPushButton('Создать новый')
        save_button = QPushButton('Сохранить файл')
        open_button = QPushButton('Открыть файл')
        self.text = QTextEdit()

        self.num_symbols = QLabel('Количество символов:')
        self.num_words = QLabel('Количество слов:')
        self.largiest_word = QLabel('Самое длинное слово:')
        self.shortiest_word = QLabel('Самое короткое слово:')
        self.often_word = QLabel('Часто встречающееся слово:')

        main_l = QHBoxLayout()
        v_l1 = QVBoxLayout()
        v_l2 = QVBoxLayout()

        v_l1.addWidget(self.input_file)
        v_l1.addWidget(new_file_button)
        v_l1.addWidget(save_button)
        v_l1.addWidget(open_button)
        v_l1.addWidget(self.num_symbols)
        v_l1.addWidget(self.num_words)
        v_l1.addWidget(self.largiest_word)
        v_l1.addWidget(self.shortiest_word)
        v_l1.addWidget(self.often_word)
        v_l2.addWidget(self.text)
        v_l1.addStretch()

        main_l.addStretch()
        main_l.addLayout(v_l1, 2)
        main_l.addLayout(v_l2, 3)
        main_l.addStretch()

        self.setLayout(main_l)

        open_button.clicked.connect(self.open_file)
        save_button.clicked.connect(self.safe_file)
        new_file_button.clicked.connect(self.new_file)

    def open_file(self):
        self.text.setText('')
        with open(self.input_file.text(), 'r', encoding='utf-8') as file:
            text = file.readlines()
            str_text = ''.join(text)
            self.text.insertPlainText(str_text)
            max_word = ''
            min_word = ''
            a = 0
            b = 99999999
            length = 0
            num_words = 0
            list_text = []
            for lines in text:
                lines = lines.rstrip('\n')
                list_lines = lines.split(' ')
                for i in list_lines:
                    list_text.append(i)
                    num_words += 1
                    length += len(i)
                    if len(i) >= a:
                        max_word = ''
                        max_word = max_word + i
                        a = len(i)
                    if len(i) < b:
                        min_word = ''
                        min_word = min_word + i
                        b = len(i)
            max_count = Counter(list_text)
            max_cont = 0
            for i in max_count:
                if max_count[i] > max_cont:
                    max_cont = max_count[i]
                    word = i
            self.largiest_word.setText(f'Самое длинное слово: {str(max_word)}')
            self.num_symbols.setText(f'Количество символов: {length}')
            self.num_words.setText(f'Количество слов: {num_words}')
            self.shortiest_word.setText(f'Самое короткое слово: {min_word}')
            self.often_word.setText(f'Часто встречающееся слово: {word}')

    def safe_file(self):
        with open(self.input_file.text(), 'r+', encoding='utf-8') as file:
            file.write(str(self.text.toPlainText()))

    def new_file(self):
        with open(self.input_file.text(), 'w', encoding='utf-8') as file:
            file.write(self.text.toPlainText())


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
