def main():
    # Задача 1
    spisok = [34, 54, 56, 23, 12, 3, 6, 67, 888]
    n = len(spisok)
    for j in range(0, n - 1):
        for i in range(n - 1):
            if spisok[i] > spisok[i + 1]:
                spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
        print(spisok)

    # Задача 2
    spisok = [34, 54, 56, 23, 12, 3, 6, 67, 888]
    for i in range(1, len(spisok)):
        for j in range(i, 0, -1):
            if spisok[j] < spisok[j - 1]:
                spisok[j], spisok[j - 1] = spisok[j - 1], spisok[j]
            else:
                break
        print(spisok)


if __name__ == '__main__':
    main()
