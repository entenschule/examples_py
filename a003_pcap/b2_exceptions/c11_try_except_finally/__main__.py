"""
python -m a003_pcap.b2_exceptions.c11_try_except_finally
"""


def f():
    try:
        raise ArithmeticError
    except:
        raise AssertionError
    finally:
        raise AttributeError
    return 'pointless'


print('The function returns:', f())


"""
ArithmeticError
During handling of the above exception, another exception occurred:
AssertionError
During handling of the above exception, another exception occurred:
AttributeError
"""
