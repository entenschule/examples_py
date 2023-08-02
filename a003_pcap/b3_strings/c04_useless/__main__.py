"""
python -m a003_pcap.b3_strings.c04_useless
"""

# This does nothing:
'spam'
'ham'
'eggs'


# One string over two lines:
foo = [
    'spam',
    'ham'
    'eggs'
]
assert foo == ['spam', 'hameggs']


# `is` has higher precedence than `not`. But this code throws SyntaxWarnings.
# assert not 'a' is 'A'
# assert 'a' is not 'A'


# numbers < uppercase < lowercase
assert '1' < 'A' < 'a'


# escape
assert len('\A') == len('\\A') == 2  # Capital A can not be encoded, and thus `\A` will (grudgingly) be printed.
assert len('\a') == 1  # This is some kind of alert character.


# Operations with None are not allowed.
try:
    None * 123
except TypeError as e:
    assert e.args[0] == "unsupported operand type(s) for *: 'NoneType' and 'int'"


# The empty string is not alphanumeric, or anything like that.
assert not ''.isalnum()
assert not ''.isdigit()
assert not ''.islower()
