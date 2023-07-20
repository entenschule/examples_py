from a001_misc.b001_slugs.c03_generator_doubled import find_duplicates, flatten, double_generator


database = {
    1: {'fruit': 'Apple', 'color': 'Red'},
    2: {'fruit': 'Apple', 'color': 'Green'},
    3: {'fruit': 'Peach', 'color': 'Yellow'},
    4: {'fruit': 'Peach', 'color': 'Green'},
    5: {'fruit': 'Plum', 'color': 'Blue'}
}

pid_to_slug = {1: 'Apple', 2: 'Apple', 3: 'Peach', 4: 'Peach', 5: 'Plum'}


def test():
    dup_gen = find_duplicates(pid_to_slug)
    dup_gen_to_test, dup_gen_to_refine = double_generator(dup_gen)

    assert list(dup_gen_to_test) == [[1, 2], [3, 4]]

    for pid in flatten(dup_gen_to_refine):
        pid_to_slug[pid] += database[pid]['color']

    assert pid_to_slug == {1: 'AppleRed', 2: 'AppleGreen', 3: 'PeachYellow', 4: 'PeachGreen', 5: 'Plum'}

