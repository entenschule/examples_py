"""
python -m a003_pcap.b4_oo.c02_isinstance
"""


class Foo:
    pass


foo = Foo()

assert isinstance(foo, Foo)  # expected

assert isinstance(foo, (Foo, list, ZeroDivisionError))  # good to know
