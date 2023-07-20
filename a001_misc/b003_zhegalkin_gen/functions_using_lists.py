from .function_shared import binary_indices


def atom(arity, atomval):
    assert atomval < arity
    length = 1 << arity  # 2 ** arity
    half_period_length = 1 << atomval  # 2 ** atomval
    period_length = half_period_length << 1  # half_period_length * 2
    result = []
    for i in range(length):
        result.append(i % period_length >= half_period_length)
    return result


def conju(arity, atomvals):
    if not atomvals:
        length = 1 << arity  # 2 ** arity
        return [True] * length  # The conjunction of no arguments is the tautology.
    atoms = [atom(arity, atomval) for atomval in atomvals]
    zipped_atoms = zip(*atoms)
    result = []
    for binary_tuple in zipped_atoms:
        result.append(0 not in binary_tuple)
    return result


def zhegalkin_twin(arity, truth_table):
    assert len(truth_table) == 1 << arity  # 2 ** arity
    conjus = [conju(arity, binary_indices(k)) for k, v in enumerate(truth_table) if v]
    zipped_conjus = zip(*conjus)
    result = []
    for binary_tuple in zipped_conjus:
        result.append(sum(binary_tuple) % 2)
    return result
