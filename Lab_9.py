def main():
    # Задача 1
    print('Введите число')
    x = input()
    y = input()
    try:
        x = int(x)
        y = int(y)
        print('Сумма:', x + y)
    except ValueError:
        print('Нужно ввести целые числа')

    # Задача 2
    print('Введите число')
    while True:
        x = input()
        y = input()
        try:
            x = int(x)
            y = int(y)
            print('Сумма:', x + y)
            break
        except ValueError:
            print('Нужно ввести целые числа')

    # Задача 3
    print('Введите число')
    x = int(input())
    y = int(input())
    try:
        z = x / y
        print('Результат деления:', int(z))
    except ZeroDivisionError:
        print('На ноль делить нельзя')

    # Задача 4
    print('Введите число')
    x = input()
    y = input()
    try:
        x = int(x)
        y = int(y)
        print('Сумма:', x + y)
        print('Результат деления:', x / y)
    except ValueError:
        print('Нужно ввести целые числа')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')

    # Задача 5
    print('Введите число')
    x = input()
    y = input()
    try:
        x = int(x)
        y = int(y)
        print('Сумма:', x + y)
        print('Результат деления:', x / y)
    except ValueError:
        print('Нужно ввести целые числа')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    finally:
        print('Выход из программы')


if __name__ == '__main__':
    main()
