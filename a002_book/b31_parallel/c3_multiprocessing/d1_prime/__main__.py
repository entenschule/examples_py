import multiprocessing


"""
python -m a002_book.b31_parallel.c3_multiprocessing.d1_prime
"""


assert __name__ == '__main__'


class PrimeProcess(multiprocessing.Process):
    def __init__(self, n, lock):
        super().__init__()
        self.n = n
        self.lock = lock

    def run(self):
        if self.n < 2:
            with self.lock:
                print('▪ That is not an integer greater 1.')
            return
        i = 2
        while i * i <= self.n:
            remainder = self.n % i
            quotient = self.n // i
            if remainder == 0:  # if n is divisible by i
                with self.lock:
                    print(f'▪ {self.n} is not prime, because it is {i} * {quotient}.')
                return
            i += 1
        with self.lock:
            print(f'▪ {self.n} is prime.')


my_processes = []

lock = multiprocessing.Lock()

user_input = input('▶ ')

while user_input != 'q':
    try:
        process = PrimeProcess(int(user_input), lock)
        my_processes.append(process)
        process.start()
    except ValueError:
        with lock:
            print('▪ That is not an integer.')

    with lock:
        user_input = input("▶ ")

for p in my_processes:
    print(p)
    p.join()
