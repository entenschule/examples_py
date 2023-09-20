import sys


exit_program = True


i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        if exit_program:
            sys.exit()
        else:
            break

print('Hello!')
