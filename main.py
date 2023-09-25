# Задача 1
film = input('Введите название фильма ')
theatre = input('Введите имя кинотеатра ')
time = input('Введите время ')
print("Билет на", film, "в", theatre, "на", time, "забронирован")

# задача 2
print('Зарплата за месяц:')
wage = int(input('>>>'))
print('Количество отработанных в выходные часов')
hours = int(input('>>>'))
print('Размер премии: ', wage * 0.01 * hours)

# Задача 3
price = input("Введите сумму:")
price = int(price)
price1 = price % 1000
price2 = price % 100
price3 = price % 10
price4 = price3 // 1
price5 = price2 // 10
price6 = price1 // 100
price7 = price // 1000
print(price4, "- по 1р")
print(price5, "- по 10р")
print(price6, "- по 100р")
print(price7, "- по 1000р")

# Задача 4
feedback = input('Оцените развлекательный комплекс: ')
# Для поиска в строке используем команду .find
word1 = feedback.find('весело')
word2 = feedback.find('увлекательно')
word3 = feedback.find('развлечения')
print('Результат анализа: ', word1, word2, word3)

# Задача 5
word = input()
print(word[-(len(word) // 2) - 1])

# Задача 6
feedback = 'Алиса и Вася, большое спасибо за теплый приём!'
name1 = feedback[0:5]
name2 = feedback[8:12]
print("Назначить премию:", name1 + ',' + name2)

# Работа со списками
# Создание списка
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Добавление элемента
numbers.append(9)
# # Удаление элемента
numbers.pop(8)
# # Срез
num = numbers[3:7]
# Перевернуть список
numbers.reverse()
numb = numbers[::-1]
# Сделать двумерный список
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Выведем цифру 5 из второго списка
print(matrix[1][1])
# Очистим список numbers
numbers.clear()

# Работа с кортежами
# Создаем пустой кортеж
empty_tuple = tuple()
# Создаем заполненный кортеж
some_tuple = ('Один', 'Два', 'Три')

# Работа с множествами
# Создаем пустое множество
abc = set()
# Создаем множество с элементами
abc = set('python')
# Добавляем в пустое множество элементы
abc.update('hi', 'world')
# Операции над множествами
A = {1, 2, 3}
B = {2, 3, 4, 5, 6}
C = A.union(B)
C = A.intersection(B)
C = A.difference(B)
C = A.symmetric_difference(B)

# Работа со словарями
# Пустой словарь
some_dict = {}
# Создаем словарь с элементами
some_dict = {'fruit1': 'apple', 'fruit2': 'pear'}
# Добавляем значение
some_dict['fruit3'] = 'orange'
# Удаляем значение
del some_dict['fruit2']
# Изменение значения
some_dict['fruit2'] = 'limon'
