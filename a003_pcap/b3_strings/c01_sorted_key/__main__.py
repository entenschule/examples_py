"""
python -m a003_pcap.b3_strings.c01_sorted_key
"""


def negate(number):
    return -number


def reverse(string):
    return string[::-1]


numbers = [0, 1, 1000, 3, 666]

strings = ['az', 'ac', 'ax', 'oa', 'ao']


assert sorted(numbers) == [0, 1, 3, 666, 1000]

assert sorted(strings) == ['ac', 'ao', 'ax', 'az', 'oa']


assert sorted(numbers, key=negate) == [1000, 666, 3, 1, 0]

assert sorted(strings, key=reverse) == ['oa', 'ac', 'ao', 'ax', 'az']


# `sorted` also has the keyword `reverse`:
assert sorted(strings, key=reverse, reverse=True) == sorted(strings, key=reverse)[::-1]
