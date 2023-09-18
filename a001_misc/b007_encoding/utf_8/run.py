character_to_encodings = {
    'a': {'ord': '0x61', 'utf-8': b'\x61'},                # Latin Small Letter A
    '┬': {'ord': '0x252c', 'utf-8': b'\xe2\x94\xac'},      # Box Drawings Light Down and Horizontal
    'Ц': {'ord': '0x426', 'utf-8': b'\xd0\xa6'},           # Cyrillic Capital Letter Tse
    'Ñ': {'ord': '0xd1', 'utf-8': b'\xc3\x91'},            # Latin Capital Letter N with Tilde
    '¥': {'ord': '0xa5', 'utf-8': b'\xc2\xa5'},            # Yen Sign
    '슥': {'ord': '0xc2a5', 'utf-8': b'\xec\x8a\xa5'},      # Hangul Syllable Seug
}

for character, encodings in character_to_encodings.items():
    [hex_ord, binary_utf8] = [encodings[_] for _ in ['ord', 'utf-8']]
    assert hex(ord(character)) == hex_ord
    assert character == chr(int(hex_ord, 16))
    assert character.encode('utf-8') == binary_utf8
    assert character == binary_utf8.decode('utf-8')


########################################################################################################################


with open('_ambiguous', 'wb') as f:
    string = "┬Ц"
    binary = string.encode('cp855')  # codepage 855 (cyrillic)
    assert binary == b'\xc2\xa5'
    f.write(binary)

with open('_ambiguous', 'rb') as f:
    binary = f.read(2)
    assert binary == b'\xc2\xa5'
    string = binary.decode('cp857')  # codepage 857 (turkish)
    assert string == '┬Ñ'

with open('_ambiguous', 'r') as f:
    assert f.read(1) == '¥'


########################################################################################################################


character_to_filename = {'a': '_a', 'Ц': '_tse', '¥': '_yen', '슥': '_seug'}


for character, filename in character_to_filename.items():
    expected_binary = character_to_encodings[character]['utf-8']

    with open(filename, 'w') as f:
        f.write(character)

    with open(filename, 'rb') as f:
        binary = f.read()
        assert binary == expected_binary

    with open(filename, 'r') as f:
        assert f.read() == character
