"""
python -m a003_pcap.b4_oo.c04_inherit.d2_subclass_with_init
"""


print('######################################### This does not work:')


class Bird:
    def __init__(self):
        self.fly = 'flap flap'


class Duck(Bird):
    def __init__(self):
        self.swim = 'paddle paddle'


duck = Duck()
print(duck.swim)

try:
    print(duck.fly)
    assert False
except AttributeError as e:
    assert str(e) == "'Duck' object has no attribute 'fly'"


print('######################################### This works:')


class Bird:
    def __init__(self):
        self.fly = 'flap flap'


class Duck(Bird):
    def __init__(self):
        super().__init__()
        self.swim = 'paddle paddle'


duck = Duck()
print(duck.fly)
print(duck.swim)


"""
######################################### This does not work:
paddle paddle
######################################### This works:
flap flap
paddle paddle
"""
