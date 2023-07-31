"""
python -m a003_pcap.b2_exceptions.c10_try_finally
"""


def f():
    try:
        print('try')
        return 0
    finally:
        print('finally')
        return 1


print('The function returns:', f())


"""
try
finally
The function returns: 1
"""
