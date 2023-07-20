from string import ascii_uppercase as alphabet
from itertools import product


database = {
    0: {'name1': 'John', 'name2': 'Spam', 'born': '1985'},  # JohnSpam85a
    1: {'name1': 'John', 'name2': 'Spam', 'born': '1985'},  # JohnSpam85b
    2: {'name1': 'John', 'name2': 'Eggs', 'born': '1991'},  # JohnEggs91
    3: {'name1': 'John', 'name2': 'Eggs', 'born': '1992'},  # JohnEggs92
    4: {'name1': 'Emma', 'name2': 'Fish', 'born': '1995'},  # EmmaFish95a
    5: {'name1': 'Emma', 'name2': 'Fish', 'born': '1995'},  # EmmaFish95b
    6: {'name1': 'Mary', 'name2': 'Beer', 'born': '2000'},  # MaryBeer
    7: {'name1': 'Mary', 'name2': 'Wine', 'born': '2000'},  # MaryWine
    8: {'name1': 'Owen', 'name2': 'Wine', 'born': '2000'},  # Owen
    9: {'name1': 'Ruth', 'name2': 'Milk', 'born': '2000'}   # Ruth
}

expected_result = {
    0: 'JohnSpam85a',
    1: 'JohnSpam85b',
    2: 'JohnEggs91',
    3: 'JohnEggs92',
    4: 'EmmaFish95a',
    5: 'EmmaFish95b',
    6: 'MaryBeer',
    7: 'MaryWine',
    8: 'Owen',
    9: 'Ruth'
}


# database with 112750 rows

db_list = []

for a, b in product(range(5), range(5)):
    row = {'name1': alphabet[a], 'name2': alphabet[b], 'born': '2000'}
    for _ in range(10):
        db_list.append(row)

for a, b, c in product(range(5, 20), range(5, 20), range(100)):
    row = {'name1': alphabet[a], 'name2': alphabet[b], 'born': str(1900 + c)}
    db_list.append(row)

for i, j in product(range(300), range(300)):
    row = {'name1': str(i) + 'x', 'name2': str(j) + 'y', 'born': '2000'}
    db_list.append(row)

long_database = {}
for i, row in enumerate(db_list):
    long_database[i] = row
