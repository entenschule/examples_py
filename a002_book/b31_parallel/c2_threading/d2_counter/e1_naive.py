import threading


"""
python -m a002_book.b31_parallel.c2_threading.d2_counter.e1_naive
"""


class CounterThread(threading.Thread):
    value = 0

    def run(self):
        for i in range(10 ** 6):
            CounterThread.value += 1


A = CounterThread()
B = CounterThread()

A.start()
B.start()

A.join()
B.join()

print(CounterThread.value)  # something like 1556822 (instead of 2000000)
