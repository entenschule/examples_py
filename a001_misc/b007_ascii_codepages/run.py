"""
┬    BOX DRAWINGS LIGHT DOWN AND HORIZONTAL

Ц    CYRILLIC CAPITAL LETTER TSE

Ñ    LATIN CAPITAL LETTER N WITH TILDE

¥    YEN SIGN
"""

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
