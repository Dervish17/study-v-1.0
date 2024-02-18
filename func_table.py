def func_table(f, max_x, max_y):
    tabl = [[eval(f.replace('x', str(i)).replace('y', str(j))) for j in range(max_y + 1)] for i in range(max_x + 1)]
    [print(*i, sep='\t') for i in tabl]

