from timeit import timeit

from .green_red import g8 as green, r8 as red

from .functions_using_lists import zhegalkin_twin as fun_list
from .functions_using_yield import zhegalkin_twin as fun_yield_raw


def fun_yield(*args): return list(fun_yield_raw(*args))


"""
python -m a001_misc.b003_zhegalkin_gen.compare_time

list took 2.542 milliseconds
yield took 2.283 milliseconds
"""


number_of_repetitions = 10000

fun_names = ['list', 'yield']

for i, fun in enumerate([fun_list, fun_yield]):
    long_time = timeit(lambda: fun(8, green) == red, number=number_of_repetitions)
    short_time = round(1000 * long_time / number_of_repetitions, 3)
    print(f'{fun_names[i]} took {short_time} milliseconds')
