from timeit import timeit


def spam(n):
    return sum([i ** 2 for i in range(1, n + 1)])


def eggs(n):
    return sum(i ** 2 for i in range(1, n + 1))


assert spam(100) == eggs(100) == 338350


number_of_repetitions = 10000

long_time = timeit(lambda: spam(100))
short_time = round(1000 * long_time / number_of_repetitions, 3)
print(f'spam took {short_time} milliseconds')  # spam took 1.938 milliseconds

long_time = timeit(lambda: eggs(100))
short_time = round(1000 * long_time / number_of_repetitions, 3)
print(f'eggs took {short_time} milliseconds')  # eggs took 2.092 milliseconds
