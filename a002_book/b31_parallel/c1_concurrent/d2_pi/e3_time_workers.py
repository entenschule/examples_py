import time
import sys
from concurrent import futures
from . import pi


"""
python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e3_time_workers threads
python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e3_time_workers processes
"""


assert __name__ == '__main__'
assert len(sys.argv) == 2
argument = sys.argv[1]
assert argument in ['threads', 'processes']

Executor = futures.ThreadPoolExecutor if argument == 'threads' else futures.ProcessPoolExecutor

print('############', argument)


number_of_addends = 10000000  # ten million


def wrapped_pi(max_workers):
    with Executor(max_workers=max_workers) as e:
        f = e.submit(pi, number_of_addends)
        return f.result()


for i in range(5):
    start = time.perf_counter()
    if i == 0:
        string = 'plain:      '
        pi(number_of_addends)
    else:
        string = f'{i}  workers:'
        wrapped_pi(i)
    print(string, '\t', time.perf_counter() - start)
