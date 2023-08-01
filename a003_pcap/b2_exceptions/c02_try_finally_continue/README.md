`python -m a003_pcap.b2_exceptions.c02_try_finally_continue`


```python
for i in range(3):
    print('----------------', i)
    try:
        print('try')
        quotient = 1 / i
        print(f'● quotient: {quotient}')
    finally:
        print('finally')
        continue
```


The ZeroDivisionError for `i = 0` is not raised, because of the `continue` in the `finally` block.<br>
It forces the return in the loop, and the saved exception is discarded.

The output looks like this:

```
---------------- 0
try
finally
---------------- 1
try
● quotient: 1.0
finally
---------------- 2
try
● quotient: 0.5
finally
```

With `break` instead of `finally` the exception is also discarded, but the loop is stopped:

``` 
---------------- 0
try
finally
```
