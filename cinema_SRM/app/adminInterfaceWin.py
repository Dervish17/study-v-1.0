from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from app.addFilmWin import AddFilm
from app.addScreeningWin import AddScreening
from database import init_db, SessionLocal
from services.screening_service import ScreeningService
from services.ticket_service import TicketService


class AdminInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show_screenings()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Администратор кинтеатра "Амур" ')
        self.setStyleSheet('background-color: #90e6e4;')
        self.setWindowIcon(QIcon('resources/54544.png'))
        button_style = """
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
                """

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

        # Кнопки
        self.button_delete = QPushButton('Удалить сеанс')
        self.button_delete.setStyleSheet(button_style)
        self.button_delete.clicked.connect(self.delete_screening)

        self.button_screening = QPushButton('Добавить сеанс')
        self.button_screening.setStyleSheet(button_style)
        self.button_screening.clicked.connect(self.add_screening)

        self.button_film = QPushButton('Добавить фильм')
        self.button_film.setStyleSheet(button_style)
        self.button_film.clicked.connect(self.add_film)

        self.button_change = QPushButton('Изменить сеанс')
        self.button_change.setStyleSheet(button_style)
        self.button_change.clicked.connect(self.change_screening)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_delete)
        layout_buttons.addWidget(self.button_screening)
        layout_buttons.addWidget(self.button_film)
        layout_buttons.addWidget(self.button_change)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

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

    def delete_screening(self):
        if self.table.selectedItems():
            selected_row = self.table.currentRow()
            screening_id = int(self.table.item(selected_row, 0).text())

            confirmation_dialog = QMessageBox()
            confirmation_dialog.setStyleSheet("background-color: white; color: black;")
            confirmation_dialog.setWindowTitle("Подтверждение удаления")
            confirmation_dialog.setText(f"Вы уверены, что хотите удалить сеанс?\n"
                                        f"ID сеанса: {screening_id}")
            confirmation_dialog.setIcon(QMessageBox.Icon.Warning)
            confirmation_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirmation_dialog.setDefaultButton(QMessageBox.StandardButton.No)
            user_response = confirmation_dialog.exec()

            if user_response == QMessageBox.StandardButton.Yes:
                init_db()
                db = SessionLocal()
                screening_service = ScreeningService(db)
                ticket_service = TicketService(db)
                ticket_service.delete_tickets(screening_id)
                screening_service.delete_screening(screening_id)

                self.table.removeRow(selected_row)
                QMessageBox.information(self, "Успешно!", "Сеанс успешно удалён.")
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Успешно!")
                msg_box.setText("Сеанс успешно удалён.")
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.setStyleSheet("background-color: white; color: black;")
                msg_box.exec()

        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Сеанс сеанс не выбран")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setStyleSheet("background-color: white; color: black;")
            msg_box.exec()

    def on_table_row_selected(self):
        row = self.table.currentRow()
        data = []
        if row != -1:
            data.append(self.table.item(row, 0).text())
            data.append(self.table.item(row, 1).text())
            data.append(self.table.item(row, 2).text())
            data.append(self.table.item(row, 3).text())
            data.append(self.table.item(row, 4).text())
        return data

    def add_screening(self):
        self.add_screening = AddScreening()

        self.add_screening.show()

    def add_film(self):
        self.add_films = AddFilm()

        self.add_films.show()

    def change_screening(self):
        self.change = AddScreening(self.on_table_row_selected())
        self.change.show()
