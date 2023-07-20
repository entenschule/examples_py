import sys
from concurrent import futures
from . import pi


"""
python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e1_results threads
python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e1_results processes
"""


assert __name__ == '__main__'
assert len(sys.argv) == 2
argument = sys.argv[1]
assert argument in ['threads', 'processes']

Executor = futures.ThreadPoolExecutor if argument == 'threads' else futures.ProcessPoolExecutor


ns = [12345678, 123456, 1234, 12]

with Executor(max_workers=4) as e:
    f_to_n = {e.submit(pi, n): n for n in ns}
    for f in futures.as_completed(f_to_n):
        n = f_to_n[f]
        print(f'{n:8} \t {f} \t {f.result()}')
