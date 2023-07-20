import pytest

from .c00_initial import find_slugs as fun0
from .c01_lambda import find_slugs as fun1
from .c02_generator import find_slugs as fun2
from .c03_generator_doubled import find_slugs as fun3
from .c04_combine import find_slugs as fun4
from .c05_with import find_slugs as fun5

from . import database, expected_result


@pytest.mark.parametrize('fun', [fun0, fun1, fun2, fun3, fun4, fun5])
def test(fun):
    assert fun(database) == expected_result

    db_slice = {_: database[_] for _ in range(0, 3)}
    assert fun(db_slice) == {0: 'JohnSpam85a', 1: 'JohnSpam85b', 2: 'JohnEggs'}

    db_slice = {_: database[_] for _ in range(7, 10)}
    assert fun(db_slice) == {7: 'Mary', 8: 'Owen', 9: 'Ruth'}
