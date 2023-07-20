import itertools
from . import find_duplicates


flatten = itertools.chain.from_iterable


def test_find_duplicates():
    arg_dict = {1: 'a', 2: 'a', 3: 'b', 4: 'c', 5: 'b'}

    result_list = [[1, 2], [3, 5]]
    assert list(find_duplicates(arg_dict)) == result_list

    for i, block in enumerate(find_duplicates(arg_dict)):
        assert block == result_list[i]

    generator = find_duplicates(arg_dict)
    assert next(generator) == [1, 2]
    assert next(generator) == [3, 5]

    result_list_flat = [1, 2, 3, 5]
    for i, pid in enumerate(flatten(find_duplicates(arg_dict))):
        assert pid == result_list_flat[i]
