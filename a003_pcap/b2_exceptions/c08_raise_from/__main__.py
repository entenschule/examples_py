"""
python -m a003_pcap.b2_exceptions.c08_raise_from
"""


try:
    raise ZeroDivisionError
except ZeroDivisionError as e:
    raise ValueError from e
