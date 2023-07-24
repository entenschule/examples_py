# primes

## console programs

### without lock

[e1_console.py](e1_console.py)

``` 
$ python -m a002_book.b31_parallel.c2_threading.d1_prime.e1_console
▶ 2648651225333063
▶ 126821609265383
▶ 874496478251477▪ 126821609265383 is prime.

▶ ▪ 874496478251477 is not prime, because it is 23760017 * 36805381.
▪ 2648651225333063 is not prime, because it is 51354299 * 51576037.
87701
▪ 87701 is prime.
```

### with lock

[e2_console_lock.py](e2_console_lock.py)<br>
(There is a similar [example using multiprocessing](../../c3_multiprocessing/d1_prime/__main__.py).)

This code seems broken by design:<br>
For easy inputs (with small prime factors) the lock is not needed.<br>
And for hard inputs it prevents the result from getting printed.<br>
Examples of hard inputs are 76580839 (prime) and 67898329 (2953 &middot; 22993).

In the following example, the result for 67898329 is only printed after entering 123.

``` 
$ python -m a002_book.b31_parallel.c2_threading.d1_prime.e2_console_lock
▶ 67898329
▶ 123
▪ 67898329 is not prime, because it is 2953 * 22993.
▪ 123 is not prime, because it is 3 * 41.
```

There is a [related question on Stackoverflow](https://stackoverflow.com/questions/76729716).
According to the answer, the lock shuts after 5ms.<br>
The time could be increased to 1 second with `sys.setswitchinterval(1)`.


## loop instead of console

[e3_loop.py](e3_loop.py)
