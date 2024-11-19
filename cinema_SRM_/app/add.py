from PyQt6.QtWidgets import *


class AddCinema(QWidget):
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

        self.button_add = QPushButton('Добавить')
        self.button_add.setStyleSheet('QPushButton {font-size: 16px; background-color: orange; color: white;}')
        self.button_add.clicked.connect(self.add_cinema)

        self.button_cancel = QPushButton('Отмена')
        self.button_cancel.setStyleSheet('QPushButton {font-size: 16px; background-color: orange; color: white;}')
        self.button_cancel.clicked.connect(self.add_cancellation)

        name_label = QLabel("Укажите название фильма:")
        cinema_hall = QLabel("Выберите зал:")
        date_label = QLabel("Укажите дату и время сеанса:")

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_add)
        layout_buttons.addWidget(self.button_cancel)

        main_layout = QVBoxLayout()
        main_layout.addWidget(name_label)
        main_layout.addWidget(self.text)
        main_layout.addWidget(cinema_hall)
        main_layout.addWidget(self.hall_selector)
        main_layout.addWidget(date_label)
        main_layout.addWidget(self.session_datetime)
        main_layout.addStretch()
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

    def add_cinema(self):
        film_name = self.text.text()
        selected_hall = self.hall_selector.currentText()
        session_time = self.session_datetime.dateTime().toString("dd-MM-yyyy HH:mm")

        if not film_name.strip():
            QMessageBox.warning(self, "Ошибка", "Введите название фильма!")
            return

        QMessageBox.information(self, "Фильм добавлен",
                                f"Фильм: {film_name}\nЗал: {selected_hall}\nСеанс: {session_time}")

    def add_cancellation(self):
        self.close()
