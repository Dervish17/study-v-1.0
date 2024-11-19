from PyQt6.QtWidgets import *
from app.add import AddCinema
from app.change import ChangeWin


class AdminInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Администратор кинтеатра "Амур" ')
        self.setStyleSheet('background-color: orange;')

        # Кнопки
        self.button_delete = QPushButton('Удалить')
        self.button_delete.setStyleSheet('QPushButton {font-size: 16px; background-color: white; color: black;}')
        self.button_delete.clicked.connect(self.delete_chinema)

        self.button_add = QPushButton('Добавить')
        self.button_add.setStyleSheet('QPushButton {font-size: 16px; background-color: white; color: black;}')
        self.button_add.clicked.connect(self.add_chinema)

        self.button_change = QPushButton('Изменить')
        self.button_change.setStyleSheet('QPushButton {font-size: 16px; background-color: white; color: black;}')
        self.button_change.clicked.connect(self.change_chinema)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_delete)
        layout_buttons.addWidget(self.button_add)
        layout_buttons.addWidget(self.button_change)

        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)

    def delete_chinema(self):
        QMessageBox.warning(self, "Удаление", f"Вы точно хотите удалить данные?"
                                              f"\nПосле удаления данные возврату не подлежат!")


    def add_chinema(self):
        self.add_cinemas = AddCinema()
        self.add_cinemas.show()

    def change_chinema(self):
        self.change = ChangeWin()
        self.change.show()
