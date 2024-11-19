from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout,
                             QHBoxLayout, QLineEdit)
from PyQt6.QtGui import QIcon
from app.admin_interface import AdminInterface


class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: orange;")
        self.setWindowTitle('Авторизация')
        self.resize(500, 400)
        self.setWindowIcon(QIcon('resources/cinema.ico'))

        authorization_label = QLabel('Авторизация')
        authorization_label.setStyleSheet('color: black')
        login_label = QLabel('Логин  ')
        password_label = QLabel('Пароль')
        self.login = QLineEdit()
        self.login.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        self.login.setPlaceholderText('Введите логин')
        self.password = QLineEdit()
        self.password.setStyleSheet("QLineEdit { color: black; background-color: white;}")
        self.password.setPlaceholderText('Введите пароль')
        self.enter_btn = QPushButton('Войти')
        self.enter_btn.setStyleSheet('QPushButton {background-color: #ffffff; color: black;}')
        self.back_btn = QPushButton('Назад')
        self.back_btn.setStyleSheet('color: black')
        self.back_btn.setIcon(QIcon('resources/Back Button.png'))

        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()
        h_l3 = QHBoxLayout()
        h_l4 = QHBoxLayout()
        h_l5 = QHBoxLayout()

        h_l1.addStretch()
        h_l1.addWidget(login_label)
        h_l1.addWidget(self.login)
        h_l1.addStretch()
        h_l2.addStretch()
        h_l2.addWidget(password_label)
        h_l2.addWidget(self.password)
        h_l2.addStretch()
        h_l3.addStretch(2)
        h_l3.addWidget(self.enter_btn, 1)
        h_l3.addStretch(2)
        h_l4.addStretch()
        h_l4.addWidget(authorization_label)
        h_l4.addStretch()
        h_l5.addWidget(self.back_btn)
        h_l5.addStretch()

        main_l.addLayout(h_l5)
        main_l.addStretch()
        main_l.addLayout(h_l4)
        main_l.addLayout(h_l1)
        main_l.addLayout(h_l2)
        main_l.addLayout(h_l3)
        main_l.addStretch()

        self.setLayout(main_l)

        self.back_btn.clicked.connect(self.go_back)
        self.enter_btn.clicked.connect(self.enter)

    def enter(self):
        """Функция для проверки пароля"""
        self.enter_admin = AdminInterface()
        self.enter_admin.show()

    def go_back(self):
        self.close()
