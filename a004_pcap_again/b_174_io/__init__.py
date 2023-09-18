with open('data.txt', 'w') as f:
    for i in range(1, 6):
        f.write(f'line {i}\n')


for x in open('data.txt', 'rt'):
    print(x)

print('########################################')

for x in open('data.txt', 'r'):
    print(x)
