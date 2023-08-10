"""
python -m a003_pcap.b4_oo.c02_isinstance
"""


class Bird:
    pass


class Duck(Bird):
    pass


bird = Bird()
duck = Duck()


assert isinstance(bird, Bird)
assert isinstance(duck, Bird)

objects = (Bird, list, ZeroDivisionError)
assert isinstance(bird, objects)
assert isinstance(duck, objects)
assert isinstance([12], objects)

objects = [Bird, list, ZeroDivisionError]
try:
    isinstance(bird, objects)
    assert False
except TypeError as e:
    assert str(e) == 'isinstance() arg 2 must be a type or tuple of types'
