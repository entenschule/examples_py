# sequence

## right

The code in [d1](d1_right.py) is similar to the [slug example](../../b001_slugs/c05_with/__init__.py).

The `Sequence` class has the attributes `sum` and `alternating_sum`.<br>
In the output below they are the second and third columns. (The sums are triangular numbers.)

``` 
1        1       1       [1]
2        3       -1      [1, 2]
3        6       2       [1, 2, 3]
4        10      -2      [1, 2, 3, 4]
5        15      3       [1, 2, 3, 4, 5]
6        21      -3      [1, 2, 3, 4, 5, 6]
7        28      4       [1, 2, 3, 4, 5, 6, 7]
8        36      -4      [1, 2, 3, 4, 5, 6, 7, 8]
```

There are two ways to achieve this:

<table>
<tr>
<th>s1</th>
<th>s2</th>
<th>s3</th>
</tr>
<tr>
<td><pre>
def __init__(self):
    self.sum = 0
    self.alternating_sum = 0
&nbsp;
def __enter__(self):
    self.list = []
    return self.list
</pre></td>
<td><pre>
    def __init__(self):
        self.sum = 0
        self.alternating_sum = 0
&nbsp;
    def __enter__(self):
        self.list = []
        return self
</pre></td>
<td><pre>
def __enter__(self):
    self.list = []
    self.sum = 0
    self.alternating_sum = 0
    return self
</pre></td>
</tr>
<tr>
<td><pre>
with sequence as sequence_list:
    for i in range(n):
        sequence_list.append(i + 1)
</pre></td>
<td colspan="2"><pre>
with sequence:
    for i in range(n):
        sequence.list.append(i + 1)
</pre></td>
</tr>
</table>

## wrong

In the wrong variant the old rows stick at the start of `list`.<br>
This happens, because `self.list = []` is moved from `__enter__` to `__init__`.<br>
But this would also work, if `sequence = Sequence()` were moved inside the loop.

``` 
1        1       1       [1]
2        4       2       [1, 1, 2]
3        10      0       [1, 1, 2, 1, 2, 3]
4        20      -2      [1, 1, 2, 1, 2, 3, 1, 2, 3, 4]
5        35      1       [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5]
6        56      4       [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
7        84      0       [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7]
8        120     -4      [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 8]
```

(The sums are tetrahedral numbers.)
