import time
import sys
from concurrent import futures
from . import pi


"""
python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e2_time
python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e2_time threads
python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e2_time processes
"""


if __name__ != "__main__":
    print('The script is not executed directly. Nothing will happen.')
else:
    start = time.perf_counter()
    numbers_of_addends = (34567890, 5432198, 44444444, 22222222, 56565656, 43236653, 23545353, 32425262)

    if len(sys.argv) == 2:
        print('############', sys.argv[1])
        if sys.argv[1] == "threads":
            with futures.ThreadPoolExecutor(max_workers=4) as e:
                results = e.map(pi, numbers_of_addends)
        elif sys.argv[1] == "processes":
            with futures.ProcessPoolExecutor(max_workers=4) as e:
                results = e.map(pi, numbers_of_addends)
        else:
            print('The script received an unexpected argument.')
    elif len(sys.argv) == 1:
        print('############ plain')
        results = map(pi, numbers_of_addends)
    else:
        print('The script received an unexpected number of arguments.')

    print(list(results))
    print(time.perf_counter() - start)
