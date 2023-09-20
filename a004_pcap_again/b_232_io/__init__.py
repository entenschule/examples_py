stuff = ['water\n', 'bred\n', 'yellow\n', 'blue\n']

f = open('text', 'w+')

f.writelines(stuff)

truncate = True
if truncate:
    f.seek(7)  # The first printed line will be "red". The ignored characters are ['w', 'a', 't', 'e', 'r', '\n', 'b'].
else:
    f.seek(0)  # The first printed line will be "water".

for line in f:
    print(line, end='')

f.close()
