def enlarge(arg_counter, arg_list, arg_number, arg_string):

    assert arg_number == 0
    assert arg_string == ''

    # mutable (will change the variables outside the function)
    arg_counter.number += 1
    arg_list.append(1)

    # immutable (no effect outside the function)
    arg_number += 1
    arg_string = arg_string + '1'

    assert arg_number == 1
    assert arg_string == '1'


class Counter:
    def __init__(self):
        self.number = 0


my_counter = Counter()
my_list = []
my_number = 0
my_string = ''

for i in range(0, 10):
    enlarge(my_counter, my_list, my_number, my_string)

assert my_counter.number == 10
assert my_list == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert my_number == 0
assert my_string == ''
