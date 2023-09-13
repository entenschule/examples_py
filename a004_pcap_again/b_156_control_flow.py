add_up = count_up = 0

while True:
    s = input('Enter a positive integer, or enter q to stop: ')
    assert s.isnumeric() or s == 'q'
    if s == 'q':
        break
    add_up += int(s)
    count_up += 1

average = add_up / count_up

average_str = format(average, '.2f')

print(f'The average is: {average_str}')
