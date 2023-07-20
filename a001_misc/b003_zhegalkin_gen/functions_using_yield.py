from .function_shared import binary_indices


def atom(arity, atomval):
    assert atomval < arity
    length = 1 << arity  # 2 ** arity
    half_period_length = 1 << atomval  # 2 ** atomval
    period_length = half_period_length << 1  # half_period_length * 2
    for i in range(length):
        yield i % period_length >= half_period_length


def conju(arity, atomvals):
    if not atomvals:
        length = 1 << arity  # 2 ** arity
        for i in range(length):
            yield True  # The conjunction of no arguments is the tautology.
    atoms = [atom(arity, atomval) for atomval in atomvals]
    zipped_atoms = zip(*atoms)
    for binary_tuple in zipped_atoms:
        yield 0 not in binary_tuple


def zhegalkin_twin(arity, truth_table):
    assert len(truth_table) == 1 << arity  # 2 ** arity
    conjus = [conju(arity, binary_indices(k)) for k, v in enumerate(truth_table) if v]
    zipped_conjus = zip(*conjus)
    for binary_tuple in zipped_conjus:
        yield sum(binary_tuple) % 2
