# slice

`python -m a003_pcap.b3_strings.c03_slice`


```python
s = '0123456789'
```

## parameters

The following table shows the default values of `start` and `stop`, depending on the sign of `step`.<br>
Default means, that the value in the table cell will do the same as `None`.

<table>
<tr>
<th></th>
<th>start</th>
<th>stop</th>
</tr>
<tr>
<th>positive step</th>
<td>0 &nbsp; (first index)</td>
<td>length &nbsp; (place after last index)</td>
</tr>
<tr>
<th>negative step</th>
<td>&minus;1 &nbsp; (last index)</td>
<td>&minus;length &minus; 1 &nbsp; (place before first index)</td>
</tr>
</table>

The last index is `length - 1` (here 9), but also `-1` by definition.<br>
Because of this definition, the place before the first index can not be called `-1`.<br>
Instead, one has to count from `-1` for the last index, which makes `-length - 1` (here &minus;11).

```python
assert s[::] == s[0:10:] == '0123456789'
assert s[::-1] == s[-1:-11:-1] == '9876543210'
```


### start 

```python
assert s[5::] == '56789'
assert s[5::-1] == '543210'
```

### stop

```python
assert s[:5:] == '01234'
assert s[:5:-1] == '9876'
```

### step

1 by default. 0 causes ValueError.

```python
assert s[::2] == '02468'
assert s[::-2] == '97531'
```
