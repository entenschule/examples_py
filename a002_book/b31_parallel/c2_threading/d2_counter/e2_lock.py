import threading


"""
python -m a002_book.b31_parallel.c2_threading.d2_counter.e2_lock
"""


class CounterThread(threading.Thread):
    value = 0
    lock = threading.Lock()

    def run(self):
        for i in range(10 ** 6):
            with CounterThread.lock:
                CounterThread.value += 1


A = CounterThread()
B = CounterThread()

A.start()
B.start()

A.join()
B.join()

print(CounterThread.value)
