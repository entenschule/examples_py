foo = [1, 2, 3]
bar = [10, 100, 1000]

my_map = map(
    lambda x, y: x * y,
    foo,
    bar
)

assert list(my_map) == [10, 200, 3000]


##########################################################


my_map = map(
    lambda x, y, z: x + y + z,
    ['a', 'b', 'c'],
    ['1', '2', '3'],
    ['x', 'y', 'z']
)

assert list(my_map) == ['a1x', 'b2y', 'c3z']
