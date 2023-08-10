"""
python -m a003_pcap.b4_oo.c03_mro.d3_all_fail
"""


def message(bases):
    return f"""Cannot create a consistent method resolution
order (MRO) for bases {bases}"""


class A(object): pass
class B(object): pass
class C(object): pass
class D(object): pass
class E(object): pass
class ABC(A, B, C): pass
class ECB(E, C, B): pass


try:
    class Foo(ABC, ECB): pass
    assert False
except TypeError as e:
    assert str(e) == message('B, C')


try:
    class Foo(ECB, ABC): pass
    assert False
except TypeError as e:
    assert str(e) == message('C, B')
