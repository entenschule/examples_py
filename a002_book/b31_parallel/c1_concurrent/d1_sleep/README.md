The tables below show the output with the `ThreadPoolExecutor` and different values of `max_workers`.

The sequence of arguments is: 9, 2, 5, 6, 3

## wait

`shutdown` with default `wait = True`

<table>
<tr>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
</tr>
<tr>
<td>
<pre>
------- 9    0
#########    0
1 of 9       1
2 of 9       2
3 of 9       3
4 of 9       4
5 of 9       5
6 of 9       6
7 of 9       7
8 of 9       8
9 of 9       9
------- 2    9
1 of 2      10
2 of 2      11
------- 5   11
1 of 5      12
2 of 5      13
3 of 5      14
4 of 5      15
5 of 5      16
------- 6   16
1 of 6      17
2 of 6      18
3 of 6      19
4 of 6      20
5 of 6      21
6 of 6      22
------- 3   22
1 of 3      23
2 of 3      24
3 of 3      25
$$$$$$$$$   25
</pre>
</td>
<td>
<pre>
------- 9    0
------- 2    0
#########    0
1 of 2       1
1 of 9       1
2 of 9       2
2 of 2       2
------- 5    2
3 of 9       3
1 of 5       3
4 of 9       4
2 of 5       4
5 of 9       5
3 of 5       5
6 of 9       6
4 of 5       6
7 of 9       7
5 of 5       7
------- 6    7
8 of 9       8
1 of 6       8
9 of 9       9
2 of 6       9
------- 3    9
3 of 6      10
1 of 3      10
4 of 6      11
2 of 3      11
5 of 6      12
3 of 3      12
6 of 6      13
$$$$$$$$$   13
</pre>
</td>
<td>
<pre>
------- 9    0
------- 2    0
------- 5    0
#########    0
1 of 9       1
1 of 5       1
1 of 2       1
2 of 5       2
2 of 2       2
2 of 9       2
------- 6    2
3 of 5       3
3 of 9       3
1 of 6       3
4 of 5       4
4 of 9       4
2 of 6       4
5 of 5       5
------- 3    5
5 of 9       5
3 of 6       5
1 of 3       6
6 of 9       6
4 of 6       6
2 of 3       7
5 of 6       7
7 of 9       7
6 of 6       8
3 of 3       8
8 of 9       8
9 of 9       9
$$$$$$$$$    9
</pre>
</td>
<td>
<pre>
------- 9    0
------- 2    0
------- 5    0
------- 6    0
#########    0
1 of 9       1
1 of 2       1
1 of 5       1
1 of 6       1
2 of 9       2
2 of 2       2
2 of 6       2
2 of 5       2
------- 3    2
3 of 9       3
3 of 5       3
3 of 6       3
1 of 3       3
4 of 9       4
4 of 5       4
2 of 3       4
4 of 6       4
5 of 9       5
5 of 5       5
3 of 3       5
5 of 6       5
6 of 9       6
6 of 6       6
7 of 9       7
8 of 9       8
9 of 9       9
$$$$$$$$$    9
</pre>
</td>
<td>
<pre>
------- 9    0
------- 2    0
------- 5    0
------- 6    0
------- 3    0
#########    0
1 of 3       1
1 of 9       1
1 of 2       1
1 of 5       1
1 of 6       1
2 of 3       2
2 of 9       2
2 of 2       2
2 of 5       2
2 of 6       2
3 of 3       3
3 of 9       3
3 of 5       3
3 of 6       3
4 of 9       4
4 of 5       4
4 of 6       4
5 of 6       5
5 of 9       5
5 of 5       5
6 of 6       6
6 of 9       6
7 of 9       7
8 of 9       8
9 of 9       9
$$$$$$$$$    9
</pre>
</td>
</tr>
</table>

## don't wait

`shutdown` with `wait = False`

Column 1 did not change (apart from the dollar signs). In column 2 `------- 5` is now before `2 of 9`.

<table>
<tr>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
</tr>
<tr>
<td>
<pre>
------- 9    0
#########    0
$$$$$$$$$    0
1 of 9       1
2 of 9       2
3 of 9       3
4 of 9       4
5 of 9       5
6 of 9       6
7 of 9       7
8 of 9       8
9 of 9       9
------- 2    9
1 of 2      10
2 of 2      11
------- 5   11
1 of 5      12
2 of 5      13
3 of 5      14
4 of 5      15
5 of 5      16
------- 6   16
1 of 6      17
2 of 6      18
3 of 6      19
4 of 6      20
5 of 6      21
6 of 6      22
------- 3   22
1 of 3      23
2 of 3      24
3 of 3      25
</pre>
</td>
<td>
<pre>
------- 9    0
------- 2    0
#########    0
$$$$$$$$$    0
1 of 2       1
1 of 9       1
2 of 2       2
------- 5    2
2 of 9       2
1 of 5       3
3 of 9       3
4 of 9       4
2 of 5       4
5 of 9       5
3 of 5       5
6 of 9       6
4 of 5       6
5 of 5       7
7 of 9       7
------- 6    7
8 of 9       8
1 of 6       8
9 of 9       9
2 of 6       9
------- 3    9
3 of 6      10
1 of 3      10
4 of 6      11
2 of 3      11
5 of 6      12
3 of 3      12
6 of 6      13
</pre>
</td>
<td>
<pre>
------- 9    0
------- 2    0
------- 5    0
#########    0
$$$$$$$$$    0
1 of 9       1
1 of 2       1
1 of 5       1
2 of 9       2
2 of 2       2
------- 6    2
2 of 5       2
3 of 9       3
1 of 6       3
3 of 5       3
4 of 9       4
4 of 5       4
2 of 6       4
5 of 9       5
5 of 5       5
------- 3    5
3 of 6       5
6 of 9       6
1 of 3       6
4 of 6       6
7 of 9       7
2 of 3       7
5 of 6       7
8 of 9       8
3 of 3       8
6 of 6       8
9 of 9       9
</pre>
</td>
<td>
<pre>
------- 9    0
------- 2    0
------- 5    0
------- 6    0
#########    0
$$$$$$$$$    0
1 of 9       1
1 of 6       1
1 of 5       1
1 of 2       1
2 of 2       2
2 of 5       2
2 of 6       2
2 of 9       2
------- 3    2
3 of 5       3
1 of 3       3
3 of 9       3
3 of 6       3
4 of 9       4
2 of 3       4
4 of 5       4
4 of 6       4
5 of 9       5
5 of 6       5
5 of 5       5
3 of 3       5
6 of 9       6
6 of 6       6
7 of 9       7
8 of 9       8
9 of 9       9
</pre>
</td>
<td>
<pre>
------- 9    0
------- 2    0
------- 5    0
------- 6    0
------- 3    0
#########    0
$$$$$$$$$    0
1 of 6       1
1 of 9       1
1 of 2       1
1 of 5       1
1 of 3       1
2 of 6       2
2 of 5       2
2 of 3       2
2 of 2       2
2 of 9       2
3 of 6       3
3 of 5       3
3 of 3       3
3 of 9       3
4 of 6       4
4 of 5       4
4 of 9       4
5 of 6       5
5 of 5       5
5 of 9       5
6 of 6       6
6 of 9       6
7 of 9       7
8 of 9       8
9 of 9       9
</pre>
</td>
</tr>
</table>


## order

With `max_workers = 5` the first rows always look like this:

```
------- 9    0
------- 2    0
------- 5    0
------- 6    0
------- 3    0
```

After that the order is random, but it is consistent within the same execution of the script:

<table>
<tr>
<td>
<pre>
1 of 3       1
1 of 9       1
1 of 2       1
1 of 5       1
1 of 6       1
2 of 3       2
2 of 9       2
2 of 2       2
2 of 5       2
2 of 6       2
</pre>
</td>
<td>
<pre>
1 of 9       1
1 of 3       1
1 of 6       1
1 of 5       1
1 of 2       1
2 of 9       2
2 of 3       2
2 of 6       2
2 of 5       2
2 of 2       2
</pre>
</td>
<td>
<pre>
1 of 9       1
1 of 2       1
1 of 3       1
1 of 6       1
1 of 5       1
2 of 9       2
2 of 2       2
2 of 3       2
2 of 6       2
2 of 5       2
</pre>
</td>
</tr>
</table>


## with ... as

These code blocks are equivalent. When `with` is used, the method `shutdown` is implicitly run with default `wait=True`.

<table>
<tr>
<td>
<pre>
e = futures.ThreadPoolExecutor(max_workers=max_workers)
&nbsp;
e.submit(f, 9)
e.submit(f, 2)
e.submit(f, 5)
e.submit(f, 6)
e.submit(f, 3)
</pre>
</td>
<td>
<pre>
with futures.ThreadPoolExecutor(max_workers=max_workers) as e:
    e.submit(f, 9)
    e.submit(f, 2)
    e.submit(f, 5)
    e.submit(f, 6)
    e.submit(f, 3)
</pre>
</td>
</tr>
</table>
