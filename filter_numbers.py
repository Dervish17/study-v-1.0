from functools import lru_cache

# def filter_numbers():
#     numbers = []
#     for i in range(int(input())):
#         if i % 3 == 0 or i % 5 == 0:
#             numbers.append(i)
#     return numbers


@lru_cache()
def filter_numbers():
    while True:
        try:
            number = int(input("Введите положительное целое число: "))
            if number > 0:
                break
            else:
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
    numbers = []
    for i in range(number + 1):
        if i % 3 == 0 or i % 5 == 0:
            numbers.append(i)
    return numbers



def filter_numbers():
    while True:
        try:
            number = int(input("Введите положительное целое число: "))
            if number > 0:
                break
            else:
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
    numbers = []
    for i in range(number + 1):
        if i % 3 == 0 or i % 5 == 0:
            numbers.append(i)
    return numbers

def filter_numbers():
    while True:
        try:
            number = int(input("Введите положительное целое число: "))
            if number > 0:
                break
            else:
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    return [i for i in range(number + 1) if i % 3 == 0 or i % 5 == 0]