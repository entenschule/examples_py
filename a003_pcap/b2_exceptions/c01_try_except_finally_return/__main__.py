"""
python -m a003_pcap.b2_exceptions.c01_try_except_finally_return
"""


def f():
    try:
        print('########### try')
        raise ArithmeticError
    except ArithmeticError:
        print('########### except')
        raise AssertionError
    finally:
        print('########### finally')
        return 123


assert f() == 123
