a = 99


########################################################################################################


def spam():
    a += 1


try:
    spam()
    assert False  # not reached, because the line before fails
except UnboundLocalError:
    pass


######################################################################################################


def foo():
    b = a
    b += 1
    return b


assert foo() == 100
assert a == 99


####################################################


def bar():
    a = 100
    return a


assert bar() == 100
assert a == 99
