"""
python -m a003_pcap.b2_exceptions.c08_raise_from
"""


try:
    raise ValueError
except ValueError as e:
    raise ZeroDivisionError from e
