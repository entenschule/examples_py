a = [1, 2, 3]


########################################################################################################


def spam():
    a += [4]


try:
    spam()
    assert False  # not reached, because the line before fails
except UnboundLocalError:
    pass


def eggs():
    a.append(4)


eggs()
assert a == [1, 2, 3, 4]


########################################################################################################


def foo_copy():
    b = a.copy()
    b += [5]
    return b


assert foo_copy() == [1, 2, 3, 4, 5]
assert a == [1, 2, 3, 4]


def foo_equals():
    b = a
    b += [5]
    return b


assert foo_equals() == a == [1, 2, 3, 4, 5]


########################################################################################################


def bar():
    a = [88, 99]
    return a


assert bar() == [88, 99]
assert a == [1, 2, 3, 4, 5]
