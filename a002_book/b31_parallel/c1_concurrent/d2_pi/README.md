The function `pi` calculates _&pi;_ using the Wallis product. It is imported from [`__init__.py`](__init__.py).

## results

[`e1_results.py`](e1_results.py)

### print finished entry

```python
for f in futures.as_completed(f_to_n):
    n = f_to_n[f]
    print(f'{n:8} \t {f} \t {f.result()}')
```

``` 
    1234         <Future at 0x7f39ea739af0 state=finished returned float>        3.1403210113038207
      12         <Future at 0x7f39ea739e50 state=finished returned float>        3.02317019200136
  123456         <Future at 0x7f39ea739a00 state=finished returned float>        3.1415799301866607
12345678         <Future at 0x7f39ea71ea90 state=finished returned float>        3.1415925263536626
```

### print whole dict

```python
for f in futures.as_completed(f_to_n):
    print(f_to_n)
```

```
{
  <Future at 0x7f619a448a90 state=running>: 12345678, 
  <Future at 0x7f619a462a00 state=finished returned float>: 123456, 
  <Future at 0x7f619a462d90 state=finished returned float>: 1234, 
  <Future at 0x7f619a462e80 state=pending>: 12
}

{
  <Future at 0x7f619a448a90 state=running>: 12345678, 
  <Future at 0x7f619a462a00 state=finished returned float>: 123456, 
  <Future at 0x7f619a462d90 state=finished returned float>: 1234, 
  <Future at 0x7f619a462e80 state=finished returned float>: 12
}

{
  <Future at 0x7f619a448a90 state=running>: 12345678, 
  <Future at 0x7f619a462a00 state=finished returned float>: 123456, 
  <Future at 0x7f619a462d90 state=finished returned float>: 1234, 
  <Future at 0x7f619a462e80 state=finished returned float>: 12
}

{
  <Future at 0x7f619a448a90 state=finished returned float>: 12345678, 
  <Future at 0x7f619a462a00 state=finished returned float>: 123456, 
  <Future at 0x7f619a462d90 state=finished returned float>: 1234, 
  <Future at 0x7f619a462e80 state=finished returned float>: 12
}
```

## compare time

[`e2_time.py`](e2_time.py)

The plain execution takes longest (28 s), with threads it is slightly faster (27 s), and with processes it is the fastest (16 s).

```
$ python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e2_time
############ plain
[3.141592608147534, 3.141592364424491, 3.1415926182443314, 3.141592582902278, 3.141592625817412, 3.1415926899176476, 3.1415927203014045, 3.1415926051448557]
28.05060630303342

$ python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e2_time threads
############ threads
[3.141592608147534, 3.141592364424491, 3.1415926182443314, 3.141592582902278, 3.141592625817412, 3.1415926899176476, 3.1415927203014045, 3.1415926051448557]
27.279607711010613

$ python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e2_time processes
############ processes
[3.141592608147534, 3.141592364424491, 3.1415926182443314, 3.141592582902278, 3.141592625817412, 3.1415926899176476, 3.1415927203014045, 3.1415926051448557]
16.648341003980022
```

## compare time by number of workers

[`e3_time_workers.py`](e3_time_workers.py)

Something is wrong here. It should be faster with parallelization,
and the number of workers should also have an influence.

``` 
$ python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e3_time_workers threads
############ threads
plain:           1.0056436459999532
1  workers:      1.0139265889883973
2  workers:      1.0425036560045555
3  workers:      1.0167908990406431
4  workers:      1.045699788024649

$ python -m a002_book.b31_parallel.c1_concurrent.d2_pi.e3_time_workers processes
############ processes
plain:           0.9996073369984515
1  workers:      1.0350342569872737
2  workers:      1.0676843019900844
3  workers:      1.057868634001352
4  workers:      1.0461909099831246

```
