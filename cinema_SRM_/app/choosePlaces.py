from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PyQt6.QtGui import QColor, QIcon


class CinemaBooking(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: orange;")
        self.setWindowTitle("Бронирование мест в кинозале")
        self.resize(800, 450)
        self.setWindowIcon(QIcon('resources/cinema.ico'))

        vbox = QVBoxLayout()

        self.table = QTableWidget(10, 20)
        self.table.setHorizontalHeaderLabels([str(i + 1) for i in range(20)])
        self.table.setVerticalHeaderLabels([chr(ord('A') + i) for i in range(10)])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.cellClicked.connect(self.on_cell_clicked)
        self.table.setStyleSheet('QHeaderView {background-color: #c0c0c0; color: black;}')

        vbox.addWidget(self.table)

        confirm_button = QPushButton("Подтвердить бронь")
        confirm_button.clicked.connect(self.confirm_booking)
        confirm_button.setStyleSheet('QPushButton {font-size: 16px; background-color: white; color: black;}')
        vbox.addWidget(confirm_button)

        self.selected_seats_label = QLabel("")
        vbox.addWidget(self.selected_seats_label)

        self.setLayout(vbox)

    def on_cell_clicked(self, row, column):
        item = self.table.item(row, column)
        if not item or not item.text():
            seat_name = f"{self.table.verticalHeaderItem(row).text()}{column + 1}"
            item = QTableWidgetItem(seat_name)
            item.setBackground(QColor("green"))
            self.table.setItem(row, column, item)
            self.selected_seats_label.setText(f"Вы выбрали место: {seat_name}")
        else:
            item.setBackground(QColor("white"))
            self.selected_seats_label.setText("")

    def confirm_booking(self):
        selected_items = []
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item and item.background().color().name() == "#008000":
                    selected_items.append(item)

        seats = ", ".join(item.text() for item in selected_items)
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Icon.Information)
        message_box.setText(f"Ваши места забронированы: {seats}")
        message_box.exec()
