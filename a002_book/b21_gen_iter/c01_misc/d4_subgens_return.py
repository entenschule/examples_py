def boys_gen():
    yield 'Boris'
    yield 'Peter'
    yield 'Oscar'
    return 3


def girls_gen():
    yield 'Susan'
    yield 'Karen'
    return 2


def names_gen(with_girls=True):
    number_of_boys = yield from boys_gen()
    print(f'There are {number_of_boys} boys.')
    if with_girls:
        number_of_girls = yield from girls_gen()
        print(f'There are {number_of_girls} girls.')


gen_with_girls = names_gen()

print(list(gen_with_girls))


"""
There are 3 boys.
There are 2 girls.
['Boris', 'Peter', 'Oscar', 'Susan', 'Karen']
"""
