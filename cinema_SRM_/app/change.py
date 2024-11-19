from PyQt6.QtWidgets import *


class ChangeWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(600, 500)
        self.setWindowTitle('Добавить фильм')

        self.text = QLineEdit()
        self.text.setMaxLength(50)
        self.text.setPlaceholderText("Введите название фильма")

        self.hall_selector = QComboBox()
        self.hall_selector.addItems(["Зал 1", "Зал 2", "Зал 3", "Зал 4", "Зал 5", "Зал 6"])

        self.session_datetime = QDateTimeEdit()

        self.button_change = QPushButton('Изменить', self)
        self.button_change.setStyleSheet('QPushButton {font-size: 16px; background-color: orange; color: white;}')
        self.button_change.clicked.connect(self.change_chinema)

        self.button_cancel = QPushButton('Отмена', self)
        self.button_cancel.setStyleSheet('QPushButton {font-size: 16px; background-color: orange; color: white;}')
        self.button_cancel.clicked.connect(self.change_cancellation)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_change)
        layout_buttons.addWidget(self.button_cancel)

        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Укажите название фильма:"))
        main_layout.addWidget(self.text)
        main_layout.addWidget(QLabel("Выберите зал:"))
        main_layout.addWidget(self.hall_selector)
        main_layout.addWidget(QLabel("Укажите дату и время сеанса:"))
        main_layout.addWidget(self.session_datetime)
        main_layout.addStretch()
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

    def change_chinema(self):
        film_name = self.text.text()
        selected_hall = self.hall_selector.currentText()
        session_time = self.session_datetime.dateTime().toString("dd-MM-yyyy HH:mm")

        if not film_name.strip():
            QMessageBox.warning(self, "Ошибка", "Введите название фильма!")
            return

        QMessageBox.information(self, "Фильм изменен",
                                f"Фильм: {film_name}\nЗал: {selected_hall}\nСеанс: {session_time}")

    def change_cancellation(self):
        self.close()
