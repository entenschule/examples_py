from . import long_database as database

from .c00_initial import find_slugs as fun0
from .c01_lambda import find_slugs as fun1
from .c02_generator import find_slugs as fun2
from .c03_generator_doubled import find_slugs as fun3
from .c04_combine import find_slugs as fun4
from .c05_with import find_slugs as fun5


"""
python -m a001_misc.b001_slugs.compare_results
"""


for i, fun in enumerate([fun0, fun1, fun2, fun3, fun4, fun5]):
    result = fun(database)
    if i == 0:
        first_result = result
    else:
        assert result == first_result
