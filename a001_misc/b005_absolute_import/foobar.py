# print('◇◇◇', __name__)
# print('◆◆◆', __file__)

from a001_misc.b005_absolute_import.foo import foo


def foobar():
    return foo() + 'bar'
