from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication
from PyQt6.QtGui import QIcon
from app.addDataWin import AddDataWin
from app.viewDataWin import ViewDataWin


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Сервисный центр')
        self.resize(300, 400)
        self.setWindowIcon(QIcon('resources/computer.ico'))
        wid = QWidget()
        self.setCentralWidget(wid)
        self.view_data_btn = QPushButton('Просмотреть')
        self.add_data_btn = QPushButton('Добавить')
        main_vl = QVBoxLayout()
        main_vl.addStretch()
        main_vl.addWidget(self.view_data_btn)
        main_vl.addWidget(self.add_data_btn)
        main_vl.addStretch()
        wid.setLayout(main_vl)
        self.view_data_btn.clicked.connect(self.show_view_data_win)
        self.add_data_btn.clicked.connect(self.show_add_data_win)

    def show_view_data_win(self):
        self.win_v = ViewDataWin()
        self.win_v.show()

    def show_add_data_win(self):
        self.win_a = AddDataWin()

    def closeEvent(self, event):
        QApplication.quit()
