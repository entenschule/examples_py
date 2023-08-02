"""
python -m a003_pcap.b4_oo.c07_change_class_variable.redefine_good
"""


class Bodyguard:
    protect = ['the king']

    def __init__(self, *args):
        if args:
            self.protect = self.protect + list(args)


"""
Bodyguards that protect specific people shall be called "specifics". The others shall be called "generics".
"""


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


# The king's title was updated for all generics, and for specifics initialized after AnnoyingBodyguard was defined.
assert bg1.protect == bg2.protect == ['his majesty the king']
assert bg_foreign.protect == ['his majesty the king', 'the foreign minister']

# But not for specifics initialized before AnnoyingBodyguard was defined.
assert bg_prime.protect == ['the king', 'the prime minister']
assert bg_foobar.protect == ['the king', 'the secretary of foo', 'the secretary of bar']


########################################################################################################################


class Bureaucrat:
    def __init__(self, name):
        Bodyguard.protect.append(name)


malfoy = Bureaucrat('Malfoy')
bg3 = Bodyguard()
bg_paper = Bodyguard('the secretary of paperwork')


# Malfoy was added for all generics.
assert bg1.protect == bg2.protect == bg3.protect == ['his majesty the king', 'Malfoy']

# And for specifics initialized after Malfoy:
assert bg_paper.protect == ['his majesty the king', 'Malfoy', 'the secretary of paperwork']

# But not for specifics initialized before Malfoy:
assert bg_prime.protect == ['the king', 'the prime minister']
assert bg_foreign.protect == ['his majesty the king', 'the foreign minister']
