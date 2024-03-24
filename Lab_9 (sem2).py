from classes.chest import Chest
from classes.button import Button
from classes.tamagotchi import Tamagotchi


def main():
    # Сундук
    big_chest = Chest('Brown', 1.5, 1, 1)
    big_chest.open_chest()
    big_chest.put_in('камень', 10)
    big_chest.put_in('камень', 5)
    big_chest.put_in('ветка', 27)
    big_chest.put_out('камень', 7)
    big_chest.put_out('ветка', 5)
    big_chest.close_chest()
    # Кнопка
    some_button = Button(50, 50, 30, 30)
    some_button.moving(60, 70)
    some_button.click()
    # Тамагочи
    cat = Tamagotchi('Кошка')
    cat.show_status()
    cat.play()
    cat.show_status()


if __name__ == '__main__':
    main()
