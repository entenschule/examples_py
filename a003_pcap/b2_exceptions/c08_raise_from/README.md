`python -m a003_pcap.b2_exceptions.c08_raise_from`


```python
try:
    raise ZeroDivisionError
except ZeroDivisionError as e:
    raise ValueError from e
```

The usual output is basically:

``` 
ZeroDivisionError
During handling of the above exception, another exception occurred:
ValueError
```

The presence of `from e` changes the sentence:

```
ZeroDivisionError
The above exception was the direct cause of the following exception:
ValueError
```

With `from None` it is only `ValueError`.