from collections import defaultdict
from string import ascii_lowercase as alphabet


def find_slugs(database):

    def maybe_finish():
        # A block is a list of PIDs with (currently) the same slug.
        slug_to_block = defaultdict(list)
        for pid, slug in pid_to_slug.items():
            slug_to_block[slug].append(pid)

        if len(slug_to_block) == len(database):
            return pid_to_slug

        nonlocal blocks_to_refine
        blocks_to_refine = [block for block in slug_to_block.values() if len(block) > 1]

    ##################################################################

    blocks_to_refine = None  # created and updated in `maybe_finish`

    pid_to_slug = dict()  # result

    # step 1: start with first name
    for pid, table_row in database.items():
        pid_to_slug[pid] = table_row['name1']

    maybe_result = maybe_finish()     ################################
    if maybe_result is not None:      ##### This is rather ugly. #####
        return maybe_result           ################################

    # step 2: add last name
    for block in blocks_to_refine:
        for pid in block:
            pid_to_slug[pid] += database[pid]['name2']

    maybe_result = maybe_finish()     ################################
    if maybe_result is not None:      ##### This is rather ugly. #####
        return maybe_result           ################################

    # step 3: add year of birth
    for block in blocks_to_refine:
        for pid in block:
            pid_to_slug[pid] += database[pid]['born'][2:4]

    maybe_result = maybe_finish()     ################################
    if maybe_result is not None:      ##### This is rather ugly. #####
        return maybe_result           ################################

    # step 4: append letter to year of birth
    for block in blocks_to_refine:
        for i, pid in enumerate(block):
            pid_to_slug[pid] += alphabet[i]

    return pid_to_slug
