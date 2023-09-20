"""
The lambda function evaluates one expression, but takes many arguments.
"""

my_sum = (lambda a, b, c, d, e: a+b+c+d+e)(1, 2, 3, 4, 5)

assert my_sum == 15
