"""
┬    BOX DRAWINGS LIGHT DOWN AND HORIZONTAL

Ц    CYRILLIC CAPITAL LETTER TSE

Ñ    LATIN CAPITAL LETTER N WITH TILDE

¥    YEN SIGN

슥    Hangul Syllable Seug
"""


# The content of this file will be the two bytes C2 AF.
with open('ambiguous.txt', 'wb') as f:
    encoded = "┬Ц".encode('cp855')
    assert encoded == b'\xc2\xa5'
    f.write(encoded)

with open('ambiguous.txt', 'rb') as f:
    encoded = f.read(2)
    decoded = encoded.decode('cp857')
    assert decoded == '┬Ñ'

with open('ambiguous.txt', 'r') as f:
    assert f.read(1) == '¥'


###################################################################


# The content of this file will also be the two bytes C2 AF.
with open('yen_sign.txt', 'w') as f:
    s = '¥'
    assert hex(ord(s)) == '0xa5'
    f.write(s)


# The content of this file will also be the three bytes EC 8A A5.
with open('hangul_syllable_seug.txt', 'w') as f:
    s = '슥'
    assert hex(ord(s)) == '0xc2a5'
    f.write(s)
