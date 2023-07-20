def squares(n):
    for i in range(1, n+1):
        yield i ** 2


class Squares:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, i):
        i += 1  # 0*0 is not very interesting ...
        if i > len(self) or i < 1:
            raise IndexError
        return i ** 2

    def __len__(self):
        return self.n


squares_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

fun_gen = squares(10)
class_gen = Squares(10)

assert list(fun_gen) == squares_list
assert list(fun_gen) == []  # second use fails

assert list(class_gen) == squares_list
assert list(class_gen) == squares_list  # second use works
