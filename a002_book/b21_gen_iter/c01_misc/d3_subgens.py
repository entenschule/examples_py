def boys_gen():
    yield 'Boris'
    yield 'Peter'


def girls_gen():
    yield 'Susan'
    yield 'Karen'


def names_gen(with_girls=True):
    yield from boys_gen()
    if with_girls:
        yield from girls_gen()


gen_with_girls = names_gen()
gen_without_girls = names_gen(False)

assert list(gen_with_girls) == ['Boris', 'Peter', 'Susan', 'Karen']

assert list(gen_without_girls) == ['Boris', 'Peter']
