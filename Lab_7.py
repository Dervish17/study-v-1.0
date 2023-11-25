def main():
    arr = list(map(int, input().split(' ')))
    dicts = []
    u = 0
    z = 0
    for a in arr:
        if a == 0:
            d = {'digits': 1, 'units': 0, 'zeros': 1}
            dicts.append(d)
        else:
            a = bin(a)
            a = a[2:]
            print(a)
            for i in a:
                if i == 1:
                    u += 1
                else:
                    z += 1
            d = {'digits': len(a), 'units': u, 'zeros': z}
            dicts.append(d)
    print(dicts)


if __name__ == '__main__':
    main()
