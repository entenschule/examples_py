# crawler

Each of these scripts will download five Wikipedia articles.<br>

* [e1_simple](e1_simple/__main__.py)
* [e2_queue](e2_queue/__main__.py)

```
python -m a002_book.b31_parallel.c4_asyncio.d2_crawler.e1_simple
python -m a002_book.b31_parallel.c4_asyncio.d2_crawler.e2_queue
```

## presidents

With `big = False` in [shared.py](shared.py) these are the outputs with only the first five presidents.

<table>
<tr>
<th>simple</th>
<th>queue</th>
</tr>
<tr>
<td>
<pre>
CRAWL 0.001
  0   0.001
  1   0.003
  2   0.004
  3   0.004
  4   0.005
▽ 4   0.445
▽ 1   0.445
▽ 0   0.445
▽ 2   0.446
▽ 3   0.654
▼ 4   1.126
▼ 2   1.278
▼ 1   1.28
▼ 0   1.696
▼ 3   1.878
○ 0   1.879
○ 1   1.883
○ 2   1.886
○ 3   1.891
○ 4   1.893
</pre>
</td>
<td>
<pre>
CRAWL 0.001
  0   0.001
  1   0.001
  2   0.001
  3   0.001
  4   0.001
▽ 0   0.491
▽ 1   0.492
▽ 2   0.494
▼ 1c1 0.873
▼ 0c0 0.883
▼ 2c2 0.892
▽ 3   0.974
▽ 4   0.993
▼ 4c0 1.127
▼ 3c1 1.137
○ 1   1.139
○ 0   1.142
○ 2   1.147
○ 4   1.151
○ 3   1.154
</pre>
</td>
</tr>
</table>

## long articles

With `big = True` the articles in [many_long_articles.py](many_long_articles.py) will be downloaded.

<table>
<tr>
<th>simple</th>
<th>queue</th>
</tr>
<tr>
<td>
<pre>
  498   0.275
  499   0.276
  500   0.276
▽ 113   0.795
▽ 158   0.918
▽ 180   1.248
</pre>
<pre>
▽ 104   2.804
▼ 113   2.82
▽ 97   2.921
</pre>
<pre>
○ 498   85.124
○ 499   85.128
○ 500   85.132
</pre>
</td>
<td>
<pre>
  498   0.026
  499   0.026
  500   0.026
▽ 0   0.273
▽ 1   0.286
▽ 2   0.294
▼ 1c1 0.496
▼ 2c2 0.596
▽ 3   0.674
▽ 4   0.906
▼ 3c1 1.032
▼ 0c0 1.079
</pre>
<pre>
○ 498   78.609
○ 499   78.614
○ 500   78.62
</pre>
</td>
</tr>
</table>