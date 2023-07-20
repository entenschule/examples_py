import itertools
from collections import defaultdict
from string import ascii_lowercase as alphabet

flatten = itertools.chain.from_iterable
def double_generator(gen): return itertools.tee(gen, 2)


def find_duplicates(pid_to_slug, dup_gen_to_refine=None):
    slug_to_pids = defaultdict(list)
    if dup_gen_to_refine is not None:
        for pid in flatten(dup_gen_to_refine):
            slug = pid_to_slug[pid]
            slug_to_pids[slug].append(pid)
    else:
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
    dup_gen = find_duplicates(pid_to_slug)
    dup_gen_to_append, dup_gen_to_refine = double_generator(dup_gen)
    for pid in flatten(dup_gen_to_append):
        pid_to_slug[pid] += database[pid]['name2']

    # step 3: add year of birth
    dup_gen = find_duplicates(pid_to_slug, dup_gen_to_refine)
    dup_gen_to_append, dup_gen_to_refine = double_generator(dup_gen)
    for pid in flatten(dup_gen_to_append):
        pid_to_slug[pid] += database[pid]['born'][2:4]

    # step 4: append letter to year of birth
    dup_gen = find_duplicates(pid_to_slug, dup_gen_to_refine)
    dup_gen_to_append, dup_gen_to_refine = double_generator(dup_gen)
    for block in dup_gen_to_append:
        for letter, pid in zip(alphabet, block):
            pid_to_slug[pid] += letter

    return pid_to_slug
