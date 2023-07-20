import threading


"""
python -m a002_book.b31_parallel.c2_threading.d1_prime.e2_console_lock
"""


class PrimeThread(threading.Thread):

    lock = threading.Lock()

    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        if self.n < 2:
            with PrimeThread.lock:  # # # # #
                print('▪ That is not an integer greater 1.')
            return
        i = 2
        while i ** 2 <= self.n:
            remainder = self.n % i
            quotient = self.n // i
            if remainder == 0:  # if n is divisible by i
                with PrimeThread.lock:  # # # # #
                    print(f'▪ {self.n} is not prime, because it is {i} * {quotient}.')
                return
            i += 1
        with PrimeThread.lock:  # # # # #
            print(f'▪ {self.n} is prime.')


my_threads = []

user_input = input('▶ ')

while user_input != 'q':
    try:
        n = int(user_input)  # raises ValueError if input string contains anything but figures (even decimal point)
        thread = PrimeThread(n)
        my_threads.append(thread)
        thread.start()
    except ValueError:
        with PrimeThread.lock:  # # # # #
            print('▪ That is not an integer.')

    with PrimeThread.lock:  # # # # #
        user_input = input('▶ ')

for t in my_threads:
    print(t)
    t.join()
