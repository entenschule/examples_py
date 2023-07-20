# print('◇◇◇', __name__)
# print('◆◆◆', __file__)

from .foo import foo


def foobar():
    return foo() + 'bar'
