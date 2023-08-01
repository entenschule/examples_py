"""
python -m a003_pcap.b2_exceptions.c04_args
"""


# single argument

try:
    raise Exception('spam')
except Exception as e:
    assert str(e) == 'spam'
    assert e.args == ('spam',)


# multiple arguments

try:
    raise Exception('spam', 'eggs')
except Exception as e:
    assert str(e) == str(e.args)
    assert e.args == ('spam', 'eggs')
