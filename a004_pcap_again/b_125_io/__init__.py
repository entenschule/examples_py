file = open('data.txt', 'w+')
print('Name of the file: ', file.name)

s = 'wxyz\naaaa\nbbbb\ncccc'
file.write(s)

file.seek(2)

for line in file:
    line = line.strip()
    print(line)

file.close()
