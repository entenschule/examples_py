"""
python -m a003_pcap.b4_oo.c07_change_class_variable.append_bad
"""


class Bodyguard:
    protectees = ['the king']

    def __init__(self, *args):
        if args:
            for arg in args:
                self.protectees.append(arg)


"""
Bodyguards without specific protectees shall be called "generics". The others shall be called "specifics".
"""


bg1 = Bodyguard()
bg_prime = Bodyguard('the prime minister')
bg_foobar = Bodyguard('the secretary of foo', 'the secretary of bar')

assert bg1.protectees == bg_prime.protectees == bg_foobar.protectees == [
    'the king', 'the prime minister', 'the secretary of foo', 'the secretary of bar'
]


########################################################################################################################


class AnnoyingBodyguard(Bodyguard):
    Bodyguard.protectees = ['his majesty the king']


bg2 = Bodyguard()
bg_foreign = Bodyguard('the foreign minister')


assert bg1.protectees == bg2.protectees == bg_foreign.protectees == bg_prime.protectees == bg_foobar.protectees == [
    'his majesty the king', 'the foreign minister'
]


########################################################################################################################


class Bureaucrat:
    def __init__(self, name):
        self.name = name
        Bodyguard.protectees.append(name)


malfoy = Bureaucrat('Malfoy')
bg3 = Bodyguard()
bg_paper = Bodyguard('the secretary of paperwork')

assert bg1.protectees == bg2.protectees == bg3.protectees == bg_paper.protectees == bg_prime.protectees == bg_foreign.protectees == [
    'his majesty the king', 'the foreign minister', 'Malfoy', 'the secretary of paperwork'
]
