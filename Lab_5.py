def main():
    # Задание 1
    numbers = ''
    for i in range(int(input())):
        numbers += input()
    print(len(set(numbers)))

    # Задание 2
    a = set(input())
    b = set(input())
    c = set(input())
    d = set.intersection(c, a)
    e = set.intersection(a, b)
    f = d | e
    print(*f, sep='')

    # Задание 3
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
    num = input()
    print(*(numbers - set(map(int, num))), sep=' ')

    # Задание 4
    nums = []
    numbers = []
    while True:
        num = int(input())
        if num == 0:
            break
        nums.append(num)
    for i in nums:
        if i % len(nums) == 0:
            numbers.append(i)
    print(numbers)

    # Задание 5
    num = int(input())
    flags = []
    for i in range(num):
        i = input()
        flags.append(i)
    for a in range(int(input())):
        print(flags[a % num])

    # Задание 8
    arr = list(map(int, input().split(' ')))
    r = []
    for a in arr:
        if a == 0:
            d = {'digits': 1, 'units': 0, 'zeros': 1}
            r.append(d)
        else:
            u = 0
            z = 0
            while a > 0:
                if a % 2 == 0:
                    z += 1
                else:
                    u += 1
                a = a // 2
            d = {'digits': u + z, 'units': u, 'zeros': z}
            r.append(d)
    print(r)


if __name__ == '__main__':
    main()
