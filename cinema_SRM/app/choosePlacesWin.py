from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView
from PyQt6.QtGui import QColor, QIcon
from database import init_db, SessionLocal
from services.ticket_service import TicketService


class CinemaBooking(QWidget):
    def __init__(self, screening_id):
        super().__init__()
        self.screening_id = screening_id
        self.initUI()
        self.load_bookings()

    def initUI(self):
        self.setWindowTitle("Бронирование мест в кинозале")
        self.resize(1200, 500)
        self.setStyleSheet('background-color: #90e6e4;')
        self.setWindowIcon(QIcon('resources/54544.png'))

        self.layout = QVBoxLayout()
        self.table_widget = QTableWidget(6, 10)
        self.table_widget.setHorizontalHeaderLabels([f"Место {i + 1}" for i in range(10)])
        self.table_widget.setVerticalHeaderLabels([f"Ряд {i + 1}" for i in range(6)])
        self.table_widget.setStyleSheet("""
                                    QTableWidget {
                                        background-color: #bbbbbb; 
                                        color: black; 
                                        font-size: 14px; 
                                        border: 1px solid black; 
                                    }
                                    QHeaderView::section {
                                        background-color: black; 
                                        color: white; 
                                        font-weight: bold;
                                        border: 1px solid #b0b0b0;
                                    }
                                """)

        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

        self.table_widget.cellClicked.connect(self.book_seat)

    def load_bookings(self):
        init_db()
        db = SessionLocal()
        ticket_service = TicketService(db)
        tickets = ticket_service.get_booked_seats(self.screening_id)

        for ticket in tickets:
            row, seat = ticket.ticket_row - 1, ticket.ticket_seat - 1
            item = QTableWidgetItem("Забронировано")
            item.setBackground(QColor("green"))
            self.table_widget.setItem(row, seat, item)
        h_header = self.table_widget.horizontalHeader()
        v_header = self.table_widget.verticalHeader()
        h_header.setStretchLastSection(True)
        v_header.setStretchLastSection(True)
        for i in range(self.table_widget.columnCount()):
            h_header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
        for i in range(self.table_widget.rowCount()):
            v_header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def book_seat(self, row, column):
        item = self.table_widget.item(row, column)

        if item is None:
            item = QTableWidgetItem()
            self.table_widget.setItem(row, column, item)

        if item.background() == QColor("green"):
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText(f"Ряд {row + 1}, Место {column + 1} уже забронировано!")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setStyleSheet("background-color: white; color: black;")
            msg_box.exec()
        else:
            item.setBackground(QColor("green"))
            item.setText("Забронировано")
            self.save_ticket(row + 1, column + 1)
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Бронирование")
            msg_box.setText(f"Ряд {row + 1}, Место {column + 1} забронировано!")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setStyleSheet("background-color: white; color: black;")
            msg_box.exec()

    def save_ticket(self, row, seat):
        init_db()
        db = SessionLocal()
        ticket_service = TicketService(db)
        ticket_service.add_ticket(screening_id=self.screening_id,
                                  ticket_row=row,
                                  ticket_seat=seat,
                                  ticket_status='booked')
