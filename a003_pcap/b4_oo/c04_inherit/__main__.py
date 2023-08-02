"""
python -m a003_pcap.b4_oo.c04_inherit
"""


print('######################################### This does not work:')


class BaseBoxer:
    def __init__(self, name):
        self.name = name
        print(f'I am {self.name}. See what I can do:')
        self.punch()  # does not take an argument

    def punch(self):
        print('(punches the air)')


class Boxer(BaseBoxer):
    def punch(self, opponent):  # called with argument
        print(f'(punches {opponent})')


BaseBoxer('Abstracto')

try:
    Boxer('Aggresso')
    assert False
except TypeError as e:
    assert str(e) == "punch() missing 1 required positional argument: 'opponent'"


print('######################################### This works:')


class BaseBoxer:
    def __init__(self, *args):
        self.name = args[0]
        self.opponent = args[1] if len(args) == 2 else None
        print(f'I am {self.name}. See what I can do:')
        self.punch(self.opponent)

    def punch(self, opponent):
        print('(punches the air)')


class Boxer(BaseBoxer):
    def punch(self, opponent):
        print(f'(punches {opponent})')


BaseBoxer('Abstracto')
Boxer('Aggresso', 'Malfoy')


"""
######################################### This does not work:
I am Abstracto. See what I can do:
(punches the air)
I am Aggresso. See what I can do:
######################################### This works:
I am Abstracto. See what I can do:
(punches the air)
I am Aggresso. See what I can do:
(punches Malfoy)
"""
