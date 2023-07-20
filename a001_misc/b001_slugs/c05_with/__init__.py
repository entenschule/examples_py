from string import ascii_lowercase as alphabet
from collections import defaultdict


class ExtractUniques:
    def __init__(self):
        self.pid_to_slug = dict()

    def __enter__(self):
        self.slug_to_block = defaultdict(list)
        return self.slug_to_block

    def __exit__(self, *unused_args):
        unique_slugs = [slug for slug, block in self.slug_to_block.items() if len(block) == 1]
        for slug in unique_slugs:
            pid = self.slug_to_block[slug][0]
            self.pid_to_slug[pid] = slug
            del self.slug_to_block[slug]


def find_slugs(database):
    extract_uniques = ExtractUniques()

    # step 1: start with first name
    with extract_uniques as slug_to_block_1:
        for pid, table_row in database.items():
            slug_to_block_1[table_row['name1']].append(pid)

    # step 2: add last name
    with extract_uniques as slug_to_block_2:
        for slug, block in slug_to_block_1.items():
            for pid in block:
                new_slug = slug + database[pid]['name2']
                slug_to_block_2[new_slug].append(pid)

    # step 3: add year of birth
    with extract_uniques as slug_to_block_3:
        for slug, block in slug_to_block_2.items():
            for pid in block:
                new_slug = slug + database[pid]['born'][-2:]
                slug_to_block_3[new_slug].append(pid)

    # step 4: append letter to year of birth
    with extract_uniques as slug_to_block_4:
        for slug, block in slug_to_block_3.items():
            for letter, pid in zip(alphabet, block):
                new_slug = slug + letter
                slug_to_block_4[new_slug].append(pid)

    return extract_uniques.pid_to_slug
