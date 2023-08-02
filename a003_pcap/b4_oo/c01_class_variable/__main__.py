"""
python -m a003_pcap.b4_oo.c01_class_variable
"""


class Monarch:
    coat_of_arms = 'lion'

    def __init__(self, name):
        self.name = name

    def flag(self):
        return f'flag with a {self.coat_of_arms}'


class Usurper(Monarch):
    coat_of_arms = 'dragon'


class ConstitutionalMonarch(Monarch):
    pass


edward = Monarch('Edward')
eric = Usurper('Eric')
william = ConstitutionalMonarch('William')


for king in [edward, eric, william]:
    print(f'{king.name} uses a {king.flag()}.')


"""
Edward uses a flag with a lion.
Eric uses a flag with a dragon.
William uses a flag with a lion.
"""
