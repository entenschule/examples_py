"""
python -m a003_pcap.b4_oo.c07_change_class_variable.addassign_bad
"""


class Bodyguard:
    protect = ['the king']

    def __init__(self, *args):
        if args:
            self.protect += list(args)


########################################################################################################################


bg1 = Bodyguard()
bg_prime = Bodyguard('the prime minister')
bg_foobar = Bodyguard('the secretary of foo', 'the secretary of bar')

assert bg1.protect == bg_prime.protect == bg_foobar.protect == [
    'the king', 'the prime minister', 'the secretary of foo', 'the secretary of bar'
]


########################################################################################################################


class AnnoyingBodyguard(Bodyguard):
    Bodyguard.protect = ['his majesty the king']


bg2 = Bodyguard()
bg_foreign = Bodyguard('the foreign minister')

assert bg1.protect == bg2.protect == bg_foreign.protect == [
    'his majesty the king', 'the foreign minister'
]
assert bg_prime.protect == bg_foobar.protect == [
    'the king', 'the prime minister', 'the secretary of foo', 'the secretary of bar'
]


########################################################################################################################


class Bureaucrat:
    def __init__(self, name):
        Bodyguard.protect.append(name)


malfoy = Bureaucrat('Malfoy')
bg3 = Bodyguard()
bg_paper = Bodyguard('the secretary of paperwork')

assert bg1.protect == bg2.protect == bg3.protect == bg_foreign.protect == bg_paper.protect == [
    'his majesty the king', 'the foreign minister', 'Malfoy', 'the secretary of paperwork'
]
assert bg_prime.protect == bg_foobar.protect == [
    'the king', 'the prime minister', 'the secretary of foo', 'the secretary of bar'
]
