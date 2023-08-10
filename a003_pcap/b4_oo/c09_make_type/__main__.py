"""
python -m a003_pcap.b4_oo.c09_make_type
"""


Bird = type('Bird', (), {'sound': 'tweet'})
Duck = type('Duck', (Bird,), {'sound': 'quack'})
DuckBird = type('DuckBird', (Duck, Bird), {})

try:
    BirdDuck = type('BirdDuck', (Bird, Duck), {})
    assert False
except TypeError as e:
    assert str(e) == """Cannot create a consistent method resolution
order (MRO) for bases Bird, Duck"""


classes = [Bird, Duck, DuckBird]

assert [c.sound for c in classes] == ['tweet', 'quack', 'quack']
assert [list(c.__dict__.keys()) for c in classes] == [
    ['sound', '__module__', '__dict__', '__weakref__', '__doc__'],
    ['sound', '__module__',                            '__doc__'],
    [         '__module__',                            '__doc__']
]
assert [c.__module__ for c in classes] == ['__main__'] * 3
assert [c.__doc__ for c in classes] == [None] * 3

assert str(Bird.__dict__['__dict__']) == "<attribute '__dict__' of 'Bird' objects>"
