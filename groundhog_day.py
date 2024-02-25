def groundhog_day(text):
    for i, (prev, curr) in enumerate(zip(text, text[1:]), 1):
        res = [i for i, (x, y) in enumerate(zip(prev, curr)) if x != y]
        if len(res) > 2:
            return (i,) + tuple(res)
    return 0, 0


a = ["Groundhog Festival in Punxsutawney.",
     "Groundhog Festival in Punksutawney.",
     "Groundhog Festivel in Punxsutowney."]
print(groundhog_day(a))


