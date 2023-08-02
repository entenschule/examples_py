"""
python -m a003_pcap.b4_oo.c03_mro
"""


def message(bases):
    return f"""Cannot create a consistent method resolution
order (MRO) for bases {bases}"""


class A: pass
class B: pass
class AB(A, B): pass
class BA(B, A): pass
class AB_A(AB, A): pass
class BA_B(BA, B): pass


try:
    class AB_BA(AB, BA): pass
    assert False
except TypeError as e:
    assert str(e) == message('A, B')


try:
    class BA_AB(BA, AB): pass
    assert False
except TypeError as e:
    assert str(e) == message('B, A')


try:
    class B_BA(B, BA): pass
    assert False
except TypeError as e:
    assert str(e) == message('B, BA')


try:
    class A_AB(A, AB): pass
    assert False
except TypeError as e:
    assert str(e) == message('A, AB')
