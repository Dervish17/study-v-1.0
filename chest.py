class Chest:
    def __init__(self, color, length, width, height):
        self.lid = False
        self.length = length
        self.width = width
        self.height = height
        self.contents = dict()
        self.color = color

    def open_chest(self):
        self.lid = True
        print('Сундук открыт')

    def close_chest(self):
        self.lid = False
        print('Сундук закрыт')

    def put_in(self, item, count):
        if self.lid is True:
            if item in self.contents:
                self.contents[item] += count
                print('В сундуке: ', self.contents)
            else:
                self.contents[item] = count
                print('В сундуке: ', self.contents)
        else:
            print('Вы не можете положить вещи, сундук закрыт')

    def put_out(self, item, count):
        if self.lid is True:
            if item in self.contents:
                self.contents[item] -= count
                print('В сундуке: ', self.contents)
            else:
                print('Этого нет в сундуке')
        else:
            print('Вы не можете взять вещи, сундук закрыт')


big_chest = Chest('Brown', 1.5, 1, 1)
big_chest.open_chest()
big_chest.put_in('камень', 10)
big_chest.put_in('камень', 5)
big_chest.put_in('ветка', 27)
big_chest.put_out('камень', 7)
big_chest.put_out('ветка', 5)
big_chest.close_chest()
