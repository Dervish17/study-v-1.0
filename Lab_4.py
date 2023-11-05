def main():
    # Задача 1
    numbers = [int(input()) for i in range(8)]
    print(*numbers, sep='')

    # Задача 2
    for i in range(int(input())):
        name = input()
        print(name, i + 1)

    # Задача 3
    date = int(input())
    step = int(input())
    for i in range(date, 32, step):
        print(i)

    # Задача 4
    letter = input()
    count = 0
    max_count = 0
    for i in range(int(input())):
        if input() == letter:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    else:
        if count > max_count:
            max_count = count
    print(max_count)

    # Задача 5
    num = int(input())
    summ = 0
    for i in range(1, summ):
        if num % i == 0:
            summ += 1
    print(summ + num)

    # задача 6
    vowels = 'аяоёэеуюыи'
    stroka = input().split()
    max_count = 0
    for word in stroka:
        count = 0
        for letter in word:
            if letter in vowels:
                count += 1
        if count > 1:
            max_count += count - 1
    print(max_count)
    # Задача 7
    word = input()
    for i in range(int(input())):
        print(word * i, '\n')

    # Задача 8
    tel = input()
    if not tel[1:].isdecimal() and not [0] == '+':
        print('Неправильный номер телефона')

    # Задача 9
    glasn = 'ауоыиэяюёе'
    soglasn = 'бвгджзйклмнпрстфхцчшщ'
    password = input().lower()
    shifr = ''
    for i in password:
        if i in glasn:
            shifr += '0'
        if i in soglasn:
            shifr += '1'
    print(shifr)

    # Задача 10
    text = input()
    s = ''
    for i in range(0, len(text), 2):
        s += text[i]
    print(s)


if __name__ == '__main__':
    main()
