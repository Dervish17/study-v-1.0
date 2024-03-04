from factorial import factorial
from fibonacci import fibonacci
from vowels import vowels
from simple import simple
from max_number import max_number


def main():
    print('Факториал этого числа:', factorial(n=int(input('Введите число: '))))
    print('Это число:', fibonacci(n=int(input('Введите порядковый номер числа Фибоначчи: '))))
    print('В этой строке', vowels(stroka=input('Введите строку: ')), 'гласных букв')
    print(simple(n=int(input('Введите число, чтобы проверить, является ли оно простым: '))))
    print(max_number([2, 4, 45, 56, 23, 4]))


if __name__ == '__main__':
    main()
