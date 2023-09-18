# coding: cp437

with open('_tse', 'r') as f:
    character = f.read()
    tse_binary = b'\xd0\xa6'
    tse_character = tse_binary.decode('utf-8')
    assert character == tse_character
    print(character)
