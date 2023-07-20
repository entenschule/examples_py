from collections import defaultdict
from string import ascii_lowercase as alphabet


def find_slugs(database):
    pid_to_slug = {pid: '' for pid in database}
    blocks_to_refine = [list(pid_to_slug)]  # single block of all pids

    step_functions = [
        lambda _, pid: database[pid]['name1'],
        lambda _, pid: database[pid]['name2'],
        lambda _, pid: database[pid]['born'][2:4],
        lambda i, _: alphabet[i],
    ]

    for step_fun in step_functions:

        for block in blocks_to_refine:
            for i, pid in enumerate(block):
                pid_to_slug[pid] += step_fun(i, pid)

        slug_to_block = defaultdict(list)
        for pid, slug in pid_to_slug.items():
            slug_to_block[slug].append(pid)

        if len(slug_to_block) == len(database):
            return pid_to_slug

        blocks_to_refine = [block for block in slug_to_block.values() if len(block) > 1]

    return pid_to_slug
