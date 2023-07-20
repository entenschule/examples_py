# slugs

The problem is described on Code Review: [Assign unique slugs to set of people. Slugs are as short as possible. (New elements only added to ensure uniqueness.)](https://codereview.stackexchange.com/questions/285146/)

The different solutions mentioned there are in the folders like
[`c00_initial`](c00_initial).

The code here and on Code Review are essentially the same, 
but some variable names are different.

These are some important concepts:
* `pid` is the ID of a person, and the row ID in the database.
* `slug` is a name like _John_ or _JohnDoe95_, that is only as long as it needs to be.
* `block` is a list of PIDs that currently have the same slug (which thus needs to be appended in the next step).

## compare time

[`compare_time.py`](compare_time.py) measures the performance.<br>
The fastest functions are 
[`fun3`](c03_generator_doubled/__init__.py) (using a doubled generator)
and [`fun5`](c05_with/__init__.py) (using the `with` keyword).

With `number_of_repetitions = 100` the script runs for approximately 90 seconds on a normal laptop.

The results do not always look the same. In the following case `fun5` takes surprisingly long:

```
fun0 took 130 milliseconds
fun1 took 202 milliseconds
fun2 took 140 milliseconds
fun3 took 109 milliseconds
fun4 took 147 milliseconds
fun5 took 121 milliseconds
```
