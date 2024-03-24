class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self. hunger = 50
        self.happiness = 50
        self.toilet = 0

    def feed(self):
        self.hunger -= 10
        self.toilet += 1
        if self.toilet == 9:
            return 'Питомец хочет в туалет'
        elif self.toilet >= 10:
            self.toilet = 0
            return 'Случилась неприятность, пожалуйста уберите!'

        self.happiness += 10

    def heal(self):
        self.health += 10
        self.happiness += 10

    def play(self):
        self.hunger += 10
        if self.hunger == 100:
            return 'Питомец умер!'
        self.happiness += 20
        self.toilet += 1

    def show_status(self):
        print(f'Имя: {self.name}')
        print(f'Голод: {self.hunger}')
        print(f'Здоровье: {self.health}')
        print(f'Счастье: {self.happiness}')
        print(f'Потребность: {self.toilet}')


cat = Tamagotchi('Кошка')
cat.show_status()
cat.play()
cat.show_status()

