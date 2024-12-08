from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QWidget, QTableWidget, QPushButton, QVBoxLayout,
                             QTableWidgetItem, QMessageBox, QHeaderView)
from app.choosePlacesWin import CinemaBooking
from database import init_db, SessionLocal
from services.screening_service import ScreeningService


class ViewCinemaUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_screenings()

    def initUI(self):
        self.setStyleSheet("background-color: #90e6e4;")
        self.setWindowTitle('Выбор фильма')
        self.resize(800, 600)
        self.setWindowIcon(QIcon('resources/54544.png'))

        self.table = QTableWidget()
        self.table.setStyleSheet("""
                    QTableWidget {
                        background-color: #bbbbbb; 
                        color: black; 
                        font-size: 17px; 
                        border: 1px solid black; 
                    }
                    QHeaderView::section {
                        background-color: black; 
                        color: white; 
                        font-weight: bold;
                        border: 1px solid #b0b0b0;
                    }
                """)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        self.booking_btn = QPushButton('Выбрать')
        self.booking_btn.setStyleSheet("""
                    QPushButton {
                        font-size: 16px; 
                        background-color: white; 
                        color: black; 
                        border: none; 
                        padding: 10px; 
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: grey;
                    }
                    QPushButton:pressed {
                        background-color: #3c3c3c;
                    }
                """)
        main_l = QVBoxLayout()

        main_l.addWidget(self.table)
        main_l.addWidget(self.booking_btn)

        self.setLayout(main_l)

        self.booking_btn.clicked.connect(self.book_places)

    def load_screenings(self):
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.show_screenings()

    def show_screenings(self):
        init_db()
        db = SessionLocal()
        screening_session = ScreeningService(db)

        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Номер сеанса', 'Название фильма', 'Начало', 'Дата', 'Зал'])

        screenings = screening_session.all_screenings()

        self.table.setRowCount(len(screenings))
        for row_idx, screening in enumerate(screenings):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(screening.screening_id)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(screening.film_name)))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(screening.screening_begin)))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(screening.screening_date)))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(screening.cinema_hall_name)))

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

    def book_places(self):
        if self.table.selectedItems():
            current_row = self.table.currentRow()
            if current_row >= 0:
                screening_id_item = self.table.item(current_row, 0)
                screening_id = screening_id_item.text() if screening_id_item else None

                if screening_id:
                    self.places = CinemaBooking(screening_id)
                    self.places.show()
                else:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Ошибка")
                    msg_box.setText("Не удалось получить ID сеанса.")
                    msg_box.setIcon(QMessageBox.Icon.Information)
                    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                    msg_box.setStyleSheet("background-color: white; color: black;")
                    msg_box.exec()
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Пожалуйста, выберите сеанс.")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setStyleSheet("background-color: white; color: black;")
            msg_box.exec()
