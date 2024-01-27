import random


def main():
    # Задача 1
    with open('lines.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) > 0:
            print(random.choice(lines))

    # Задача 2
    with open('prices.txt', 'r', encoding='utf-8') as file:
        price = 0
        lines = file.readlines()
        for i in lines:
            i = i.split('\t')
            price += float(i[2]) * float(i[1])
        print(f'{price:.2f}')
        if len(lines) == 0:
            print('Файл пустой!')

    # Задача 3
    with open('lines.txt', 'r', encoding='utf-8') as file:
        chet = []
        nechet = []
        lines = file.readlines()
        for i in lines:
            i = i.rstrip('\n')
            if len(i) % 2 == 0:
                chet.append(i)
            else:
                nechet.append(i)
        # Первый вариант вывода: делает правильный вывод
        print('Четные строки:')
        print(*chet, sep='\n')
        print('Нечетные строки')
        print(*nechet, sep='\n')
        # Второй вариант вывода:
        print('Четные строки:', '\n', *chet, '\n', 'Нечетные строки', '\n', *nechet, sep='')

    # Задача 4
    with open('words.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        max_word = []
        a = 0
        for i in lines:
            i = i.rstrip('\n')
            if len(i) >= a:
                max_word.append(i)
                a = len(i)
        print(*max_word)

    # Задача 5
    with open('input.txt', 'r', encoding='utf-8') as file:
        lines = file.read()
        size_bit = len(lines)
        size_b = size_bit / 8
        size_kb = size_b / 1024
        size_mb = size_kb / 1024
        size_gb = size_mb / 1024
        print(size_b)
        if size_b < 1024:
            print(f'Файл весит: {size_b:1f} байт')
        if size_kb < 1024:
            print(f'Файл весит: {size_kb:1f} кбайт')
        if size_mb < 1024:
            print(f'Файл весит: {size_mb:1f} мбайт')
        if size_gb < 1024:
            print(f'Файл весит: {size_gb:1f} гбайт')


if __name__ == '__main__':
    main()
