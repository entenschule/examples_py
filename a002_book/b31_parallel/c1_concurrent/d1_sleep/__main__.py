from concurrent import futures
from time import sleep, time


"""
python -m a002_book.b31_parallel.c1_concurrent.d1_sleep
"""


max_workers = 3
wait = True

Executor = futures.ThreadPoolExecutor
# Executor = futures.ProcessPoolExecutor


tick = int(time())


def tock():
    return str(int(time()) - tick).rjust(2)


def f(t):
    print(f'------- {t}   {tock()}')
    for i in range(t):
        sleep(1)
        print(f'{i+1} of {t}      {tock()}')


e = Executor(max_workers=max_workers)

e.submit(f, 9)
e.submit(f, 2)
e.submit(f, 5)
e.submit(f, 6)
e.submit(f, 3)

print(f'#########   {tock()}')
e.shutdown(wait)
print(f'$$$$$$$$$   {tock()}')

