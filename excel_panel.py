from PyQt6.QtWidgets import QWidget, QComboBox, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, \
    QHBoxLayout, QFileDialog, QApplication
import csv


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000, 600)
        self.setWindowTitle('Результаты олимпиады: фильтрация')

        self.school_combo = QComboBox()
        self.class_combo = QComboBox()
        self.school_combo.addItem('Школа', 'all_schools')
        self.school_combo.addItem('01')
        self.school_combo.addItem('02')
        self.school_combo.addItem('03')
        self.class_combo.addItem('Класс', 'all_classes')
        self.class_combo.addItem('09')
        self.class_combo.addItem('10')
        self.class_combo.addItem('11')
        self.table = QTableWidget()
        self.result_button = QPushButton('Узнать результаты')
        self.select_file_btn = QPushButton('Выберете файл')

        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()

        main_l.addLayout(h_l1)
        main_l.addLayout(h_l2)
        h_l1.addWidget(self.school_combo)
        h_l1.addWidget(self.class_combo)
        h_l1.addWidget(self.result_button)
        h_l1.addWidget(self.select_file_btn)
        h_l2.addWidget(self.table)

        self.setLayout(main_l)

        self.school_combo.currentIndexChanged.connect(self.load_school)
        self.class_combo.currentIndexChanged.connect(self.load_class)
        self.result_button.clicked.connect(self.load_values)
        self.select_file_btn.clicked.connect(self.select_file)

    def load_class(self):
        query_type = self.class_combo.currentText()
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        if query_type == "all_classes":
            self.load_values()
        elif query_type == "09":
            self.load_values('09')
        elif query_type == "10":
            self.load_values('10')
        elif query_type == "11":
            self.load_values('11')

    def load_school(self):
        query_type = self.school_combo.currentText()
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        if query_type == "all_schools":
            self.load_values()
        elif query_type == "01":
            self.load_values('01')
        elif query_type == "02":
            self.load_values('02')
        elif query_type == "03":
            self.load_values('03')

    def load_values(self, school=None):
        self.read_csv(school)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Фамилия', 'Результат', 'Логин'])
        self.table.setRowCount(len(self.students))
        row = 0
        for student in self.students:
            self.table.setItem(row, 0, QTableWidgetItem(student['family']))
            self.table.setItem(row, 1, QTableWidgetItem(student['result']))
            self.table.setItem(row, 2, QTableWidgetItem(student['login']))
            row += 1

    def select_file(self):
        self.selected_file = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]

    def read_csv(self, school):
        with open(self.selected_file, 'r', encoding='utf-8') as csv_file:
            self.new_reader = []
            self.reader = csv.reader(csv_file, delimiter=',')
            for row in list(self.reader):
                self.new_reader.append(row)
            self.students = []
            if school:
                for row in self.new_reader[1:]:
                    if row[1].split(' ')[1] == school:
                        data = {}
                        data['family'] = row[1].split(' ')[3]
                        data['result'] = row[-1]
                        data['login'] = row[1]
                        self.students.append(data)
            else:
                for row in self.new_reader[1:]:
                    data = {}
                    data['family'] = row[1].split(' ')[3]
                    data['result'] = row[-1]
                    data['login'] = row[1]
                    self.students.append(data)


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
