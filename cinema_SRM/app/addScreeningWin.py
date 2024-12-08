from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDateTime
from database import init_db, SessionLocal
from services.screening_service import ScreeningService
from app.filmsWin import FilmWin


class AddScreening(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.initUI()
        self.data = data
        self.init_db = init_db()
        self.db = SessionLocal()
        if data:
            self.upload_editable_data()

    def initUI(self):
        self.resize(600, 600)
        self.setWindowTitle('Добавление сеанса')
        self.setWindowIcon(QIcon('resources/54544.png'))

        self.film_name = QLineEdit()
        self.film_name.setMaxLength(50)
        self.film_name.setPlaceholderText('Введите номер фильма (см. в "Справка")')
        self.film_name.setStyleSheet("padding: 5px; font: 12pt Arial;")

        self.hall_selector = QComboBox()
        self.hall_selector.addItems(["Зал 1", "Зал 2", "Зал 3", "Зал 4", "Зал 5", "Зал 6"])
        self.hall_selector.setStyleSheet("padding: 5px; font: 12pt Arial;")

        self.session_date = QLineEdit(QDateTime.currentDateTime().toString("dd.MM.yyyy"))
        self.session_date.setPlaceholderText('dd.MM.yyyy')
        self.session_date.setStyleSheet("padding: 5px; font: 12pt Arial;")

        self.session_time = QLineEdit(QDateTime.currentDateTime().toString("hh:mm"))
        self.session_time.setPlaceholderText('HH:mm')
        self.session_time.setStyleSheet("padding: 5px; font: 12pt Arial;")

        self.button_add = QPushButton('Добавить')
        self.button_add.setStyleSheet("padding: 10px; font: 12pt Arial; background-color: #90e6e4; color: black;")
        self.button_add.clicked.connect(self.add_cinema)

        self.button_cancel = QPushButton('Отмена')
        self.button_cancel.setStyleSheet("padding: 10px; font: 12pt Arial; background-color: #90e6e4; color: black;")
        self.button_cancel.clicked.connect(self.add_cancellation)

        self.films_btn = QPushButton('Справка')
        self.films_btn.clicked.connect(self.films)
        self.films_btn.setStyleSheet("padding: 10px; font: 12pt Arial; background-color: #90e6e4; color: black;")

        name_label = QLabel("Укажите номер фильма:")
        cinema_hall = QLabel("Выберите зал:")
        date_label = QLabel("Укажите дату сеанса (dd.MM.yyyy):")
        time_label = QLabel("Укажите время сеанса (HH:mm):")

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_add)
        layout_buttons.addWidget(self.button_cancel)
        name_film_layout = QHBoxLayout()
        name_film_layout.addWidget(self.film_name)
        name_film_layout.addWidget(self.films_btn)

        main_layout = QVBoxLayout()
        main_layout.addWidget(name_label)
        main_layout.addLayout(name_film_layout)
        main_layout.addWidget(cinema_hall)
        main_layout.addWidget(self.hall_selector)
        main_layout.addWidget(date_label)
        main_layout.addWidget(self.session_date)
        main_layout.addWidget(time_label)
        main_layout.addWidget(self.session_time)
        main_layout.addStretch()
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

    def upload_editable_data(self):
        self.screening_id = int(self.data[0])
        self.film_name.setText(self.data[1])
        self.hall_selector.setCurrentText(self.data[4])
        self.session_date.setText(self.data[3])
        self.session_time.setText(self.data[2])

    def add_cinema(self):
        film_name = self.film_name.text()
        selected_hall = int(self.hall_selector.currentText()[len("Зал "):])
        session_date = self.session_date.text()
        session_time = self.session_time.text()

        if not film_name.strip():
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Введите название фильма!")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setStyleSheet("background-color: white; color: black;")
            msg_box.exec()
            return
        try:
            screening_service = ScreeningService(self.db)
            if self.data is None:
                screening_service.add_screening(
                    film_id=film_name,
                    cinema_hall_id=selected_hall,
                    screening_begin=session_time,
                    screening_date=session_date
                )
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Сеанс добавлен")
                msg_box.setText(f"Сеанс добавлен")
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.setStyleSheet("background-color: white; color: black;")
                msg_box.exec()
            else:
                screening_service.update_screening(self.screening_id, film_id=film_name, cinema_hall_id=selected_hall,
                                                   screening_begin=session_time, screening_date=session_date)
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Изменения сохранены")
                msg_box.setText(f"Изменения в сеансе успешно сохранены.")
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.setStyleSheet("background-color: white; color: black;")
                msg_box.exec()
        except ValueError:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Введите корректный рейтинг!")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setStyleSheet("background-color: white; color: black;")
            msg_box.exec()


    def films(self):
        self.film_names = FilmWin()
        self.film_names.show()

    def add_cancellation(self):
        self.close()
