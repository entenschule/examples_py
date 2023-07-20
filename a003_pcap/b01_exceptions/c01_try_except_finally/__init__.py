def f():
    try:
        print('try ', end='')
        raise ArithmeticError
    except:
        print('except ', end='')
        raise AssertionError
    finally:
        print('finally')
        return


f()
