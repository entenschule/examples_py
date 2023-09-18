import random


"""
python -m a003_pcap.b1_modpack.c02_random
"""


foods = ['spam', 'ham', 'eggs']

print('########################### initial list:', foods)

code_strings = [
    'random()',  # some float with integral part 0

    'choice(foods)',  # some entry from foods
    'choices(foods)',  # list with one entry from foods
    'choices(foods, k=2)',  # list with two (not necessarily different) entries from foods
    'choices(foods, weights=[10, 1, 1], k=10)',  # list of length 10 with mostly 'spam'
    'sample(foods, k=1)',
    'sample(foods, k=2)',
    'shuffle(foods)',  # changes variable, no return value

    'randint(1000, 1005)',  # 1000 <= result <= 1005
    'randrange(1000, 1005)',  # 1000 <= result < 1005
]

for code_string in code_strings:
    print(code_string, '  ', eval('random.' + code_string))


print('########################### initial list: shuffled list', foods)


# The following code shows, that sequence of results is always the same, when the same seed is used.

for i in range(10):
    random.seed(123)
    results = []
    for j in range(10):
        result = random.random()
        results.append(result)
    if i == 0:
        first_results = results
    else:
        assert results == first_results


for i in range(10):
    random.seed(123)
    results = []
    for j in range(10):
        result = random.choices(foods, weights=[10, 1, 1], k=10)
        results.append(result)
    if i == 0:
        first_results = results
    else:
        assert results == first_results
