"""
python -m a003_pcap.b4_oo.c07_change_class_variable.reassign_better
"""


class Bodyguard:
    protect = ['the king']

    def __init__(self, *args):
        self.protect = self.protect[:]
        if args:
            self.protect = self.protect + list(args)


########################################################################################################################


bg1 = Bodyguard()
bg_prime = Bodyguard('the prime minister')
bg_foobar = Bodyguard('the secretary of foo', 'the secretary of bar')


assert bg1.protect == ['the king']
assert bg_prime.protect == ['the king', 'the prime minister']
assert bg_foobar.protect == ['the king', 'the secretary of foo', 'the secretary of bar']


########################################################################################################################


class AnnoyingBodyguard(Bodyguard):
    Bodyguard.protect = ['his majesty the king']


bg2 = Bodyguard()
bg_foreign = Bodyguard('the foreign minister')


# The king's title was updated for guards initialized after AnnoyingBodyguard was defined.
assert bg2.protect == ['his majesty the king']
assert bg_foreign.protect == ['his majesty the king', 'the foreign minister']

# But not for those initialized before.
assert bg1.protect == ['the king']
assert bg_prime.protect == ['the king', 'the prime minister']
assert bg_foobar.protect == ['the king', 'the secretary of foo', 'the secretary of bar']


########################################################################################################################


class Bureaucrat:
    def __init__(self, name):
        Bodyguard.protect.append(name)


malfoy = Bureaucrat('Malfoy')
bg3 = Bodyguard()
bg_paper = Bodyguard('the secretary of paperwork')


# Malfoy was added for guards initialized after Malfoy.
assert bg3.protect == ['his majesty the king', 'Malfoy']
assert bg_paper.protect == ['his majesty the king', 'Malfoy', 'the secretary of paperwork']

# But not for those initialized before.
assert bg2.protect == ['his majesty the king']
assert bg_foreign.protect == ['his majesty the king', 'the foreign minister']
assert bg1.protect == ['the king']
assert bg_prime.protect == ['the king', 'the prime minister']
assert bg_foobar.protect == ['the king', 'the secretary of foo', 'the secretary of bar']
