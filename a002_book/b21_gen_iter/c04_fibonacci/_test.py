from a002_book.b21_gen_iter.c04_fibonacci.classes import FiboIter, Gold, FiboYield, FiboMulti


f_list = [1, 1, 2, 3, 5]

fy = FiboYield(5)
fm = FiboMulti(5)


def test_list():

    fi = FiboIter(5)
    assert list(fi) == f_list
    assert list(fi) == []  # second use fails

    g = Gold(5)
    assert [str(_) for _ in g] == ['1', '1/2', '2/3', '3/5', '5/8']
    assert [str(_) for _ in g] == []  # second use fails

    assert list(fy) == f_list
    assert list(fy) == f_list  # second use works

    assert list(fm) == f_list
    assert list(fm) == f_list  # second use works


def test_sum():

    fi = FiboIter(5)
    assert sum(fi) == 12
    assert sum(fi) == 0  # second use fails

    assert sum(fy) == 12
    assert sum(fy) == 12  # second use works

    assert sum(fm) == 12
    assert sum(fm) == 12  # second use works


def test_matrix():

    for f in [fy, fm]:
        for key_a, val_a in enumerate(f):
            for key_b, val_b in enumerate(f):
                assert val_a == f_list[key_a]
                assert val_b == f_list[key_b]
