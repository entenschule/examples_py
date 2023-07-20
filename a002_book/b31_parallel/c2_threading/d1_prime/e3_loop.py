import threading


"""
python -m a002_book.b31_parallel.c2_threading.d1_prime.e3_loop
"""


numbers = [867612071523907, 4374553, 101009583613]


class PrimeThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        if type(self.n) != int or self.n < 2:
            print(f'● {self.n} is not a valid input.')
            return
        i = 2
        while i ** 2 <= self.n:
            remainder = self.n % i
            quotient = self.n // i
            if remainder == 0:  # if n is divisible by i
                print(f'● {self.n} is not prime, because it is {i} * {quotient}.')
                return
            i += 1
        print(f'● {self.n} is prime.')


my_threads = []

for n in numbers:
    print(' ', n)
    thread = PrimeThread(n)
    my_threads.append(thread)
    print('  ', thread)
    thread.start()

print('--------------------------------------------------------')

for t in my_threads:
    print(t)
    t.join()


"""
The console output looks like this:

  867612071523907
   <PrimeThread(Thread-1, initial)>
  4374553
   <PrimeThread(Thread-2, initial)>
● 4374553 is prime.
  101009583613
   <PrimeThread(Thread-3, initial)>
--------------------------------------------------------
<PrimeThread(Thread-1, started 139659605726976)>
● 101009583613 is not prime, because it is 168013 * 601201.
● 867612071523907 is prime.
<PrimeThread(Thread-2, stopped 139659597334272)>
<PrimeThread(Thread-3, stopped 139659597334272)>
"""
