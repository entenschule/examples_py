"""
┬    BOX DRAWINGS LIGHT DOWN AND HORIZONTAL

Ц    CYRILLIC CAPITAL LETTER TSE

Ñ    LATIN CAPITAL LETTER N WITH TILDE

¥    YEN SIGN

슥    Hangul Syllable Seug
"""


# The content of this file will be the two bytes C2 A5.
with open('AMBIGUOUS.txt', 'wb') as f:
    encoded = "┬Ц".encode('cp855')  # codepage 855 (cyrillic)
    assert encoded == b'\xc2\xa5'
    f.write(encoded)

with open('AMBIGUOUS.txt', 'rb') as f:
    encoded = f.read(2)
    decoded = encoded.decode('cp857')  # codepage 857 (turkish)
    assert decoded == '┬Ñ'

with open('AMBIGUOUS.txt', 'r') as f:
    assert f.read(1) == '¥'


###################################################################


# The content of this file will also be the two bytes C2 A5.
with open('yen.txt', 'w') as f:
    s = '¥'
    assert hex(ord(s)) == '0xa5'
    f.write(s)


# The content of this file will be the three bytes EC 8A A5.
with open('seug.txt', 'w') as f:
    s = '슥'
    assert hex(ord(s)) == '0xc2a5'
    f.write(s)


# The content of this file will be the byte 61.
with open('a.txt', 'w') as f:
    s = 'a'
    assert hex(ord(s)) == '0x61'
    f.write(s)

# The content of this file will be the six bytes 61 C2 A5 EC 8A A5.
with open('a_yen_seug.txt', 'w') as f:
    s = 'a¥슥'
    f.write(s)
