import csv
import sys


def main():
    # Задача 1
    with open('wares.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        summa = 1000
        f = []
        for row in reader:
            if int(row[1]) <= summa:
                f.append(row[0])
                count = summa // int(row[1])
                print(*f * count, sep=', ')

    # Задача 2
    with open('vps.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        procent = int(input())
        for i in list(reader)[1:]:
            if int(i[-2]) >= procent:
                print(i[0])

    # Задача 3
    with open('wares1.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for i in list(reader)[1:]:
            if int(i[1]) > int(i[2]):
                print(i[0])

    # Задача 4
    with open('exam.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['Фамилия', 'Имя', 'Результат1', 'Результат2', 'Результат3', 'Сумма'])
        n, m = map(int, input().split())
        while True:
            stroki = sys.stdin.readline().rstrip('\n')
            if stroki == '':
                break
            surname, name, result1, result2, result3 = stroki.split()
            result1, result2, result3 = int(result1), int(result2), int(result3)
            summa = result1 + result2 + result3
            if summa >= n and result1 >= m and result2 >= m and result3 >= m:
                writer.writerow([surname, name, result1, result2, result3, summa])


if __name__ == '__main__':
    main()
