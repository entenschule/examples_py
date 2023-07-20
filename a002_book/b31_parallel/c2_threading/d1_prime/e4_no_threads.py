"""
python -m a002_book.b31_parallel.c2_threading.d1_prime.e4_no_threads
"""


def is_prime(n):
    if n < 2:
        return False, None

    if n in (2, 3):
        return True,

    for i in (2, 3):
        if not n % i:
            return False, i, n // i

    i = 5
    while i * i <= n:
        for d in (0, 2):
            if not n % (i + d):
                return False, (i + d), n // (i + d)
        i += 6
    return True,


while (user_input := input('▶ ')) != 'q':
    try:
        prime_info = is_prime(int(user_input))
        if prime_info[0]:
            print(f'▪ {user_input} is a prime')
        elif prime_info[1]:
            a, b = prime_info[1:]
            print(f'▪ {user_input} is not a prime, because it is {a} * {b}')
        else:
            print(f'▪ {user_input} is not greater than 1')
    except ValueError:
        print(f'▪ {user_input} is not an integer')
