def simple(n, delit=None):
    if delit is None:
        delit = n - 1
    while delit >= 2:
        if n % delit == 0:
            return False
        else:
            return simple(n, delit - 1)
    else:
        return True
