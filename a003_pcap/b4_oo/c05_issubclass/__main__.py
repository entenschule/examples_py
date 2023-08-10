"""
python -m a003_pcap.b4_oo.c05_issubclass
"""


class A: pass
class B: pass
class C: pass
class AB(A, B): pass


assert issubclass(A, A)
assert issubclass(A, (A, B))
assert issubclass(AB, A)
assert issubclass(AB, (A, B))
assert issubclass(AB, (B, C))

try:
    issubclass((AB, C), B)
    assert False
except TypeError as e:
    assert str(e) == 'issubclass() arg 1 must be a class'
