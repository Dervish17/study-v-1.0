def vowels(stroka):
    if not stroka:
        return 0
    elif stroka[0].lower() in 'аоуыэеёиюя':
        return 1 + vowels(stroka[1:])
    else:
        return vowels(stroka[1:])
