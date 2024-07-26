import timeit

import numpy as np


def old_code():
    numbers = [i for i in range(1, 1000001)]
    squares = []
    for number in numbers:
        squares.append(number ** 2)


def optimize_code_1():
    squares = [number**2 for number in range(1, 1000001)]


def optimize_code_2():
    squares = [number*number for number in range(1, 1000001)]


def optimize_code_3():
    squares = np.square(np.arange(1, 1000001)).tolist()


def optimize_code_4():
    squares = np.square(np.arange(1, 1000001))


time = timeit.repeat("old_code()", "from __main__ import old_code", repeat=300, number=1)
print(f'Исходный код выполняется в среднем за {np.mean(time)} секунд')

time = timeit.repeat("optimize_code_1()", "from __main__ import optimize_code_1", repeat=300, number=1)
print(f'Оптимизированный код 1 выполняется в среднем за {np.mean(time)} секунд')

time = timeit.repeat("optimize_code_2()", "from __main__ import optimize_code_2", repeat=300, number=1)
print(f'Оптимизированный код 2 выполняется в среднем за {np.mean(time)} секунд')

time = timeit.repeat("optimize_code_3()", "from __main__ import optimize_code_3", repeat=300, number=1)
print(f'Оптимизированный код 3 выполняется в среднем за {np.mean(time)} секунд')

time = timeit.repeat("optimize_code_4()", "from __main__ import optimize_code_4", repeat=300, number=1)
print(f'Оптимизированный код 4 выполняется в среднем за {np.mean(time)} секунд')
