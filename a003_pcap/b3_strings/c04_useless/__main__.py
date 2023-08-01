"""
python -m a003_pcap.b3_strings.c04_useless
"""

# This does nothing:
'spam'
'ham'
'eggs'

# This is stupid:
foo = [
    'spam',
    'ham'
    'eggs'
]

assert foo == ['spam', 'hameggs']
