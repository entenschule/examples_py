`python -m a003_pcap.b2_exceptions.c01_try_except_finally_return`


The AssertionError is not raised, because of the `return` in the `finally` block.


Without the `return` these errors would be shown:

``` 
ArithmeticError
During handling of the above exception, another exception occurred:
AssertionError
```
