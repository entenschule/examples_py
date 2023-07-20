from classes import FiboYield as Fibo, Gold


def fibo_fun(n):
    assert type(n) == int and n >= 1
    gen = Fibo(n)
    for i in range(n):
        result = gen.__next__()
    return result


assert list(Fibo(10)) \
       == [fibo_fun(n) for n in range(1, 11)] \
       == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

assert sum(Fibo(10)) == 143


#######################################################################################


def gold_fun(n):
    assert type(n) == int and n >= 1
    gen = Gold(n)
    for i in range(n):
        result = gen.__next__()
    return result


assert [str(_) for _ in Gold(10)] \
       == [str(gold_fun(n)) for n in range(1, 11)] \
       == ['1', '1/2', '2/3', '3/5', '5/8', '8/13', '13/21', '21/34', '34/55', '55/89']
