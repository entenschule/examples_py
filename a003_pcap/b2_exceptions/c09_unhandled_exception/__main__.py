"""
python -m a003_pcap.b2_exceptions.c09_unhandled_exception
"""


class Menace(Exception):
    pass


try:
    raise Exception
except Menace:
    print('except')
else:
    print('else')
