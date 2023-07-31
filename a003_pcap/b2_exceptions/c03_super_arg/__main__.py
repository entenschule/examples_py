"""
python -m a003_pcap.b2_exceptions.c03_super_arg
"""


class AgeException(Exception):

    def __init__(self, age, bribe=0):

        assert self.args in [
            (age,),          # AgeException(123)
            (age, bribe)     # AgeException(123, 456)
        ]

        age_warning = f'Something seems to be wrong with age {age}.'
        super().__init__(age_warning)
        assert self.args == super().args == (age_warning,)

        self.bribe_response = 'Anyway, you can pass.' if bribe > 99 else 'Sorry.'


print('############################# Try without bribe:')

try:
    raise AgeException(16)
except AgeException as e:
    print(e)
    print(e.bribe_response)

print('############################# Try with insufficient bribe:')

try:
    raise AgeException(16, 99)
except AgeException as e:
    print(e)
    print(e.bribe_response)

print('############################# Try with sufficient bribe:')

try:
    raise AgeException(16, 100)
except AgeException as e:
    print(e)
    print(e.bribe_response)


"""
############################# Try without bribe:
Something seems to be wrong with age 16.
Sorry.
############################# Try with insufficient bribe:
Something seems to be wrong with age 16.
Sorry.
############################# Try with sufficient bribe:
Something seems to be wrong with age 16.
Anyway, you can pass.
"""
