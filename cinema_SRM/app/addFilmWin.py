from PyQt6.QtCore import QDateTime
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox, QTimeEdit, QDateTimeEdit, QPushButton, QHBoxLayout, \
    QVBoxLayout, QLabel, QMessageBox

from database import init_db, SessionLocal
from services.film_service import FilmService


class AddFilm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init_db = init_db()
        self.db = SessionLocal()

    def initUI(self):
        self.resize(600, 600)
        self.setWindowTitle('Добавить фильм')
        self.setWindowIcon(QIcon('resources/54544.png'))

        self.text = QLineEdit()
        self.text.setMaxLength(50)
        self.text.setPlaceholderText("Введите название фильма")
        self.text.setStyleSheet("padding: 5px; font: 12pt Arial;")

        self.author = QLineEdit()
        self.author.setMaxLength(50)
        self.author.setPlaceholderText("Введите имя режиссера")
        self.author.setStyleSheet("padding: 5px; font: 12pt Arial;")

        self.genre = QComboBox()
        self.genre.addItems(["Драма", "Комедия", "Ужасы", "Фантастика", "Боевик", "Романтика"])
        self.genre.setStyleSheet("padding: 5px; font: 12pt Arial;")

        self.session_time = QTimeEdit()
        self.session_time.setStyleSheet("padding: 5px; font: 12pt Arial;")

        self.session_datetime = QDateTimeEdit(QDateTime.currentDateTime())
        self.session_datetime.setCalendarPopup(True)
        self.session_datetime.setStyleSheet("padding: 5px; font: 12pt Arial;")

        self.rating = QLineEdit()
        self.rating.setPlaceholderText("Введите рейтинг фильма")
        self.rating.setStyleSheet("padding: 5px; font: 12pt Arial;")

        self.button_add = QPushButton('Добавить', self)
        self.button_add.setStyleSheet("padding: 10px; font: 12pt Arial; background-color: #90e6e4; color: black;")
        self.button_add.clicked.connect(self.add_cinema)

        self.button_cancel = QPushButton('Отмена', self)
        self.button_cancel.setStyleSheet("padding: 10px; font: 12pt Arial; background-color: #90e6e4; color: black;")
        self.button_cancel.clicked.connect(self.add_cancellation)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_add)
        layout_buttons.addWidget(self.button_cancel)

        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Укажите название фильма:"))
        main_layout.addWidget(self.text)
        main_layout.addWidget(QLabel("Укажите имя режиссера:"))
        main_layout.addWidget(self.author)
        main_layout.addWidget(QLabel("Выберите жанр:"))
        main_layout.addWidget(self.genre)
        main_layout.addWidget(QLabel("Выберете, сколько длится сеанс:"))
        main_layout.addWidget(self.session_time)
        main_layout.addWidget(QLabel("Укажите дату и время релиза:"))
        main_layout.addWidget(self.session_datetime)
        main_layout.addWidget(QLabel("Укажите рейтинг фильма:"))
        main_layout.addWidget(self.rating)
        main_layout.addStretch()
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

    def add_cinema(self):
        film_name = self.text.text()
        film_author = self.author.text()
        film_genre = self.genre.currentText()
        film_time = self.session_time.time().toString()
        film_release = self.session_datetime.dateTime().toString("dd.MM.yyyy HH:mm")

        film_rating = self.rating.text()

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
            film_service = FilmService(self.db)
            films = film_service.get_names_films()
            film_names = [film.film_name for film in films]
            print(film_names)
            film_service.add_film(
                                 film_name=film_name,
                                 film_author=film_author,
                                 film_genre=film_genre,
                                 film_time=str(film_time),
                                 film_release=str(film_release),
                                 film_rating=float(film_rating)
                                 )
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Фильм добавлен")
            msg_box.setText(f"Фильм: {film_name}\n"
                f"Режиссер: {film_author}\n"
                f"Жанр: {film_genre}\n"
                f"Длительность: {film_time}\n"
                f"Релиз: {film_release}\n"
                f"Рейтинг: {film_rating}")
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

    def add_cancellation(self):
        self.close()
