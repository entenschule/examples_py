import itertools
from collections import defaultdict
from string import ascii_lowercase as alphabet


flatten = itertools.chain.from_iterable


def find_duplicates(pid_to_slug):
    """returns generator of blocks, which are lists of PIDs with (currently) the same slug"""
    slug_to_pids = defaultdict(list)
    for pid, slug in pid_to_slug.items():
        slug_to_pids[slug].append(pid)
    for block in slug_to_pids.values():
        if len(block) > 1:
            yield block


def find_slugs(database):
    pid_to_slug = {}  # result

    # step 1: start with first name
    for pid, table_row in database.items():
        pid_to_slug[pid] = table_row['name1']

    # step 2: add last name
    for pid in flatten(find_duplicates(pid_to_slug)):
        pid_to_slug[pid] += database[pid]['name2']

    # step 3: add year of birth
    for pid in flatten(find_duplicates(pid_to_slug)):
        pid_to_slug[pid] += database[pid]['born'][2:4]

    # step 4: append letter to year of birth
    for block in find_duplicates(pid_to_slug):
        for letter, pid in zip(alphabet, block):
            pid_to_slug[pid] += letter

    return pid_to_slug
