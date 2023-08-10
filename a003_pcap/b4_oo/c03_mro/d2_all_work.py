from itertools import permutations

"""
python -m a003_pcap.b4_oo.c03_mro.d2_all_work
"""


class A(object): pass
class B(object): pass
class C(object): pass
class D(object): pass
class E(object): pass
class ABC(A, B, C): pass
class DBE(D, B, E): pass
class DA(D, A): pass


for x, y, z in permutations([ABC, DBE, DA]):
    class Foo(x, y, z): pass
