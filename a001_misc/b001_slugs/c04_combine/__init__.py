import itertools
from collections import defaultdict
from string import ascii_lowercase as alphabet

flatten = itertools.chain.from_iterable
def double_generator(gen): return itertools.tee(gen, 2)


def find_duplicates(pid_to_slug, dup_gen_to_refine):
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

    step_functions = [
        lambda _, pid: database[pid]['name1'],
        lambda _, pid: database[pid]['name2'],
        lambda _, pid: database[pid]['born'][2:4],
        lambda i, _: alphabet[i]
    ]

    pid_to_slug = {pid: '' for pid in database}
    dup_gen_to_refine = None

    for step_fun in step_functions:
        dup_gen = find_duplicates(pid_to_slug, dup_gen_to_refine)
        dup_gen_to_append, dup_gen_to_refine = double_generator(dup_gen)
        for block in dup_gen_to_append:
            for i, pid in enumerate(block):
                pid_to_slug[pid] += step_fun(i, pid)

    return pid_to_slug
