class Button:
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.press = False

    def moving(self, x, y):
        self.x = x
        self.y = y
        print(f'Кнопка перемещена в место {self.x} px на {self.y} px')

    def click(self):
        self.press = True
        print('Вы нажали на кнопку')


some_button = Button(50, 50, 30, 30)
some_button.moving(60, 70)
some_button.click()
