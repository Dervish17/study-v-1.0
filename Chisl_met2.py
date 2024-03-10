from scipy import optimize
import math
import numpy as np


def f(x):
    e = math.e
    return math.pow(e, x) - 3 * math.pow(x, 0.5)


def df(x):
    e = math.e
    return math.pow(e, x) - 1.5 * math.pow(x, -0.5)


solution = optimize.root_scalar(f, bracket=[0.5, 3], method="bisect")
etalon = solution.root
iterations_et = solution.iterations
print(f'Эталонный корень методом половинного деления: {etalon} с {iterations_et} попытки')


def bisection_method(f, a, b, tol=1e-10, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError('Функция должна иметь разные знаки на концах интервала')
    count = 0
    while (b - a) / 2 > tol and count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        count += 1
    return (a + b) / 2, count


root_bisect, count = bisection_method(f, 0.5, 3)
print(f'Корень уравнения (метод пол. дел.): {root_bisect} c {count} попытки')


def chord_method(f, a, b, eps=1e-10, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError('Функция должна иметь разные знаки на границах интервала')

    x = a - (b - a) * f(a) / (f(b) - f(a))
    count = 0
    for _ in range(max_iter):
        if np.abs(f(x)) < eps:
            break
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        x = a - (b - a) * f(a) / (f(b) - f(a))
        count += 1
    return x, count


root_chord, iterations_chord = chord_method(f, 0.5, 3)
print(f'Корень уравнения (хорд): {root_chord} с {iterations_chord} попытки')


def newton_method(f, df, x0, epsilon=1e-10, max_iter=100):
    x1 = 0
    iter_count = 0
    while iter_count < max_iter:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < epsilon:
            break
        x0 = x1
        iter_count += 1
    return x1, iter_count


x0 = 3
root, iterations_newt = newton_method(f, df, x0)

print(f'Корень уравнения (метод касательных (Ньютона): {root} с {iterations_newt} попытки')
