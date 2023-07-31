"""
python -m a003_pcap.b2_exceptions.c04_args
"""


try:
    raise Exception('spam', 'eggs')
except Exception as e:
    assert str(e) == str(e.args)
    assert e.args == ('spam', 'eggs')
