def horse2(cell):
    alphabet = 'abcdefgh'
    steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    x = alphabet.find(cell[0]) + 1
    y = int(cell[1])
    for xy in steps:
        x1, y1 = x + xy[0], y + xy[1]
        if 0 < x1 < 9 and 0 < y1 < 9:
            print(f'{alphabet[x1 - 1]}{y1}')



