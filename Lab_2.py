# Задача 1
check = input()
if check == 'Python':
    print('ДА')
else:
    print('НЕТ')

# Задача 2
a = input()
b = input()
if a == 'да' or a == 'нет' and b == 'да' or b == 'нет':
    print('ВЕРНО')
else:
    print('НЕВЕРНО')

#  Задача 3
a = input()
b = input()
c = input()
if a == 'один' or a == '1':
    if b == 'два' or b == '2':
        if c == 'три' or c == '3':
            print('ГОРИ')
else:
    print('НЕ ГОРИ')

# Задача 4
yuly = input('Введите название города для поездки в ИЮЛЕ: ')
august = input('Введите название города для поездки в АВГУСТЕ: ')
if yuly == 'Пенза' and august != 'Пенза' or yuly == 'Тула' and august != 'Тула':
    print('ДА')
else:
    print('НЕТ')

# Задача 5
n = int(input())
m = int(input())
day = n % m
if day == 0:
    print(n // m)
else:
    print(n // m + 1)

# Задача 6
num1 = int(input())
num2 = int(input())
num3 = int(input())
summa = num1 + num3 // 8
if summa != 0 and num2 == 3:
    print('Подходит')
else:
    print(num1 + num3, ' ', num2)

# Задача 7
category = input('Категория: ')
if category == 'продукты':
    price = int(input('Цена: '))
    if price < 100:
        print('Попробуйте нашу выпечку!')
    if 100 <= price < 500:
        print('Как насчёт орехов в шоколаде?')
    if price > 500:
        print('Попробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома')

# Задача 8
price1 = int(input('Цена первого товара:\n>>>'))
price2 = int(input('Цена второго товара:\n>>>'))
price3 = int(input('Цена третьего товара:\n>>>'))
summa = price1 + price2 + price3
if price1 < price2 < price3:
    print('Акция!')
    print('К оплате:', summa / 2)
if price1 > price2 > price3:
    print('Акция!')
    print('К оплате:', summa / 3)

# Задача 9
a = int(input('Введите число покупателей позавчера:\n>>>'))
b = int(input('Введите число покупателей вчера:\n>>>'))
if b > a:
    print('Сегодня магазин посетит:', b + (b - a), 'человек')
if a > b:
    print('Сегодня магазин посетит:', b - (a - b), 'человек')

# Задача 10
year = int(input('Введите год: '))
if year % 4 != 0:
    print('Год не високосный.')
else:
    print('Год високосный.')

# Задача 11
number = int(input('Введите число:'))
if number % 2 == 0:
    print('Число чётное')
else:
    print('Число нечетное')
