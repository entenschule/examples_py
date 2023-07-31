`python -m a003_pcap.b2_exceptions.c07_default_except_must_be_last`


This is not allowed:


```python
try:
    be_optimistic()
except:
    oh_no()
except ValueError:
    too_late()
```


Any specific `except` after an empty one is a SyntaxError:<br>
`SyntaxError: default 'except:' must be last`


`except BaseException` and `except Exception` are also essentially empty.<br>
But they do not have this restriction.
