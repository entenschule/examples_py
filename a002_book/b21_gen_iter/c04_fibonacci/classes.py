from fractions import Fraction


class FiboIter:
    def __init__(self, n):
        self.n, self.i, self.val, self.val_after = n, 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            self.i += 1
            self.val, self.val_after = self.val_after, self.val + self.val_after
            return self.val
        else:
            raise StopIteration


class Gold(FiboIter):
    def __next__(self):
        super().__next__()
        return Fraction(self.val, self.val_after)


class FiboYield:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        val, val_after = 0, 1
        for i in range(self.n):
            val, val_after = val_after, val + val_after
            yield val


class FiboMulti:
    class FiboIter:  # just like the `FiboIter` class above
        def __init__(self, n):
            self.n, self.i, self.val, self.val_after = n, 0, 0, 1

        def __iter__(self):
            return self

        def __next__(self):
            if self.i < self.n:
                self.i += 1
                self.val, self.val_after = self.val_after, self.val + self.val_after
                return self.val
            else:
                raise StopIteration

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self.FiboIter(self.n)
