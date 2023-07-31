`python -m a003_pcap.b2_exceptions.c11_try_except_finally`


All errors are raised. The output looks basically like this:

```
ArithmeticError
During handling of the above exception, another exception occurred:
AssertionError
During handling of the above exception, another exception occurred:
AttributeError
```


If the return were indented into the `finally` clause, it would still be pointless.<br>
But if it were moved up before the `raise`, no error would be raised.