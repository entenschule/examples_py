with open('data.txt', 'w') as f:
    f.write('aaaa\nbbbb\ncccc')


file = open('data.txt', 'r')
s = file.read(7)
assert list(s) == ['a', 'a', 'a', 'a', '\n', 'b', 'b']
