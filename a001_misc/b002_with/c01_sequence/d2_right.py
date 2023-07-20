"""
python -m a001_misc.b002_with.c01_sequence.d2_right
"""


class Sequence:

    def __init__(self):
        self.sum = 0
        self.alternating_sum = 0

    def __enter__(self):
        self.list = []
        return self

    def __exit__(self, *unused_args):
        self.sum = sum(self.list)

        alternating_sum = 0
        for key, val in enumerate(self.list):
            pos_or_neg_one = 1 - 2 * (key % 2)
            alternating_sum += pos_or_neg_one * val
        self.alternating_sum = alternating_sum


sequence = Sequence()

for n in range(1, 9):

    with sequence:
        for i in range(n):
            sequence.list.append(i + 1)

    print(n, '\t', sequence.sum, '\t', sequence.alternating_sum, '\t', sequence.list)
