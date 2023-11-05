def main():
    # Задача 1
    tape = input()
    while len(tape) > 0:
        print(len(tape))
        tape = input()
    print('Конец')

    # # Задача 2
    count = 0
    number = float(input('Введите число: '))
    while number != 36.6:
        if number < 0:
            count += 1
        number = float(input('Введите число: '))
        if number >= 36.6:
            break
    print(count)

    # Задача 3
    max_n = 0
    n = int(input())
    while 0 < n < 1000:
        if n > max_n:
            max_n = n
        n = int(input())
    print(max_n)

    # Задача 4
    i = 999999999
    a = 0
    nums = list(map(int, input().split()))
    print(nums)
    while a < len(nums):
        if nums[a] < i:
            i = nums[a]
        a += 1
    print(i)

    # Задача 5
    while True:
        number = int(input())
        if number == 0:
            break
        elif number % 7 == 0 and number % 3 == 0:
            print('Караул!')
            break
        elif number % 3 == 0:
            print('несчастливое!')
        elif number % 7 == 0:
            print('опасное!')
        else:
            print(number)

    # Задача 6
    a = 0
    summa = 0
    while a < 1000:
        a += 1
        summa = (a * (a + 1)/2)
        print(int(summa))

    # Задача 7
    print('Введите габариты большой коробки: ')
    x = int(input('Ширина: '))
    y = int(input('Длина: '))
    z = int(input('Высота: '))
    boxes = 0
    while True:
        print('Введите габариты маленьких коробок: : ')
        a = int(input('Ширина: '))
        b = int(input('Длина: '))
        c = int(input('Высота: '))
        if a == 0:
            break
        if a > x or b > y or c > z:
            print('Ошибка, попробуйте еще')
        else:
            boxes += 1
    print(boxes)

    # Задача 8
    word = input()
    i = ''
    a = 999999999
    while word != 'стоп':
        if len(word) < a:
            i = word
            a = len(word)
        word = input()
    print(i)

    # задача 9
    a = int(input('Число: '))
    b = input('Операция (стоп - завершить): ')
    i = int(input('Число:'))
    while b != 'стоп':
        if b == '+':
            i += a
        elif b == '-':
            i -= a
        elif b == '*':
            i *= a
        elif b == '/':
            i /= a
        print('Результат: ', i)
        b = input('Операция (стоп - завершить): ')
        a = int(input('Число: '))


if __name__ == '__main__':
    main()
