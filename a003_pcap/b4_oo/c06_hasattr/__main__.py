"""
python -m a003_pcap.b4_oo.c06_hasattr
"""


class Soldier:
    uniform_color = 'green'

    def __init__(self, name):
        self.name = name


class Bodyguard(Soldier):
    uniform_color = 'blue'
    protectees = ['the king']

    def __init__(self, name, nickname=None, protectees=None):
        super().__init__(name)
        self.nickname = nickname if nickname is not None else name
        if protectees:
            self.protectees += protectees


arthur = Soldier('Arthur')
robert = Bodyguard('Robert', 'Bob', ['the prime minister'])
thomas = Bodyguard('Thomas')


attribute_names = ['uniform_color', 'name', 'nickname', 'protectees']

# The soldier does not have the attributes specific to bodyguards.
assert [hasattr(arthur, _) for _ in attribute_names] == [True, True, False, False]

for bodyguard in [robert, thomas]:
    assert [hasattr(bodyguard, _) for _ in attribute_names] == [True] * 4
