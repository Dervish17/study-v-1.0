from PyQt6.QtWidgets import (QWidget, QTableWidget, QLabel, QPushButton, QVBoxLayout,
                             QHBoxLayout)
from PyQt6.QtGui import QIcon
from app.choosePlaces import CinemaBooking


class ViewCinemaUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: orange;")
        self.setWindowTitle('Выбор фильма')
        self.resize(800, 600)
        self.setWindowIcon(QIcon('resources/cinema.ico'))

        self.table = QTableWidget()
        self.table.setStyleSheet('QTableWidget {background-color: #c0c0c0; color: black;}')
        self.booking_btn = QPushButton('Выбрать')
        self.booking_btn.setStyleSheet('QPushButton {font-size: 16px; background-color: white; color: black;}')

        main_l = QVBoxLayout()

        main_l.addWidget(self.table)
        main_l.addWidget(self.booking_btn)

        self.setLayout(main_l)

        self.booking_btn.clicked.connect(self.book_places)

    def book_places(self):
        self.places = CinemaBooking()
        self.places.show()
