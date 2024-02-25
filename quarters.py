def quarters(*data):
    quarts = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}
    for x, y in data:
        if not x or not y:
            continue
        elif x > 0 and y > 0:
            quarts['I'] = quarts.get('I') + 1
        elif x < 0 and y > 0:
            quarts['II'] = quarts.get('II') + 1
        elif x < 0 and y < 0:
            quarts['III'] = quarts.get('III') + 1
        elif x > 0 and y < 0:
            quarts['IV'] = quarts.get('IV') + 1
    return quarts


data = [(1, 1), (-1, 2), (-3, -1)]
for k, v in sorted(quarters(*data).items()):
    print(f'{k}:{v}')
