# _find_ and _rfind_

`python -m a003_pcap.b3_strings.c02_find`


```python
#             x   x     x
#           012345678901234
haystack = 'Spam Ham Panama'
needle = 'am'

assert haystack.find(needle) == 2      # start 0, stop 15
assert haystack.find(needle, 2) == 2   # start 2, stop 15
assert haystack.find(needle, 3) == 6   # start 3, stop 15

assert haystack.rfind(needle) == 12          # start 0, stop 15
assert haystack.rfind(needle, 0, 14) == 12   # start 0, stop 14
assert haystack.rfind(needle, 0, 13) == 6    # start 0, stop 13
```

`needle` is in positions 2, 6 and 12 of `haystack`.

Both functions use the optional arguments `start` (0 by default) and `end` (length + 1 by default) to define the search area as `haystack[start:end]`. (So the names are somewhat misleading for `rfind`).

`find` looks for `needle` from the left of `haystack`, while `rfind` looks from the right.

For `find` the argument `start` is more important.<br>
For `rfind` the argument `end` is more important. But it can not be set without `start`.<br>
It is important to keep in mind that `rfind` with two arguments sets only `start`.
