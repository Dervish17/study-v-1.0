def main():
    # Задача 1
    arr = [9, 7, 3, 8, 4, 3, 6]
    a = len(arr)
    b = 3
    for i in range(a):
        if arr[i] == b:
            print(i)
    # Задача 2
    arr = [9, 3, 6, 7, 5, 4, 2]
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    print(arr)
    mid = len(arr) // 2
    low = 0
    high = len(arr) - 1
    value = 4
    while arr[mid] != value and low <= high:
        if value > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        print("No value")
    else:
        print("ID =", mid)

    # Задача 3
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value = 3
    fib1 = 0
    fib2 = 1
    fib = fib1 + fib2
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    index = -1
    while fib > 1:
        i = min(index + fib2, (len(arr) - 1))
        if arr[i] < value:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            index = i
        elif arr[i] > value:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            continue
    if (fib1 and index < (len(arr) - 1)) and (arr[index + 1] == value):
        print(index + 1)


if __name__ == '__main__':
    main()
