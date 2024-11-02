from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QImage, QPixmap, QColor, QTransform
from PIL import Image


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(700, 500)
        self.setWindowTitle('Изменение картинки')

        file_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.image = Image.open(file_name)
        self.save = 'rotated.png'

        self.pixmap = QPixmap(self.save)

        self.slider = QSlider(Qt.Orientation.Vertical, self)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.slider.setRange(0, 255)
        self.slider.setValue(255)
        self.slider.setSingleStep(1)

        self.label = QLabel()
        self.label.setPixmap(self.pixmap)

        button_R = QPushButton('R')
        button_G = QPushButton('G')
        button_B = QPushButton('B')
        button_ALL = QPushButton('ALL')
        button_POCH = QPushButton('По часовой стрелке')
        button_PRCH = QPushButton('Против часовой стрелки')

        main_l = QHBoxLayout()
        v_l1 = QVBoxLayout()
        v_l2 = QVBoxLayout()
        v_l3 = QVBoxLayout()
        h_l1 = QHBoxLayout()

        main_l.addStretch()
        v_l1.addStretch(1)
        v_l1.addWidget(self.slider, 7)
        v_l1.addStretch(1)
        v_l2.addWidget(self.label)
        h_l1.addWidget(button_PRCH)
        h_l1.addWidget(button_POCH)
        v_l2.addLayout(h_l1)
        main_l.addLayout(v_l1)
        main_l.addLayout(v_l2)
        v_l3.addWidget(button_R)
        v_l3.addWidget(button_G)
        v_l3.addWidget(button_B)
        v_l3.addWidget(button_ALL)
        main_l.addLayout(v_l3)
        main_l.addStretch()

        self.setLayout(main_l)

        self.slider.valueChanged[int].connect(self.visibility)
        button_PRCH.clicked.connect(self.rotate_left)
        button_POCH.clicked.connect(self.rotate_right)

    def visibility(self, value):
        self.image = self.image.convert('RGBA')
        self.image.putalpha(value)
        self.image.save(self.save)
        self.pixmap = QPixmap(self.save)
        self.label.setPixmap(self.pixmap)

    def change_RGB(self):
        pass

    def rotate_left(self):
        img = self.image.rotate(90)
        img.save(self.save)
        self.pixmap = QPixmap(self.save)
        self.label.setPixmap(self.pixmap)

    def rotate_right(self):
        img = self.image.rotate(-90)
        img.save(self.save)
        self.pixmap = QPixmap(self.save)
        self.label.setPixmap(self.pixmap)


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
