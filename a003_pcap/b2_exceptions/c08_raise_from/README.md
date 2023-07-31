`python -m a003_pcap.b2_exceptions.c08_raise_from`


```python
try:
    raise ValueError
except ValueError as e:
    raise ZeroDivisionError from e
```

The usual output is basically:

``` 
ValueError
During handling of the above exception, another exception occurred:
ZeroDivisionError
```

The presence of the `from e` changes the sentence in the middle to this:

``` 
The above exception was the direct cause of the following exception:
```

With `from None` it is only `ZeroDivisionError`.