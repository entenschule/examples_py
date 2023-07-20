from .green_red import g3, r3, g8, r8

from .functions_using_lists import zhegalkin_twin as fun_list
from .functions_using_yield import zhegalkin_twin as fun_yield_raw


def fun_yield(*args): return list(fun_yield_raw(*args))


"""
a001_misc.b003_zhegalkin_gen.compare_results
"""


def fun_yield(*args): return list(fun_yield_raw(*args))


for fun in [fun_list, fun_yield]:
    for arity, green, red in [(3, g3, r3), (8, g8, r8)]:
        assert fun(arity, green) == red
        assert fun(arity, red) == green
