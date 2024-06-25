import time


class Field:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length

    def game_over(self):
        pass


class Cell(Field):
    def __init__(self, weight, length, cell_weight, cell_length):
        super().__init__(weight, length)
        self.cell_weight = cell_weight
        self.cell_length = cell_length

    def press(self):
        pass


class Bomb(Cell):
    def __init__(self,weight, length, cell_weight, cell_length, amount):
        super().__init__(weight, length, cell_weight, cell_length)
        self.amount = amount

    def detonation(self):
        pass


class Number(Cell):
    def __init__(self, weight, length, cell_weight, cell_length, number, color_number):
        super().__init__(weight, length, cell_weight, cell_length)
        self.number = number
        self.color_number = color_number


class EmptyCell(Cell):
    def __init__(self, weight, length, cell_weight, cell_length):
        super().__init__(weight, length, cell_weight, cell_length)


class Timer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 0

    def up_time(self):
        while True:
            self.timer += 1
            time.sleep(1)

