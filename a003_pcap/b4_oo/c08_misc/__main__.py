"""
python -m a003_pcap.b4_oo.c08_misc
"""


class Spam:
    def __str__(self):
        return 'S P A M'


spam = Spam()
assert str(spam) == spam.__str__() == 'S P A M'
assert spam.__repr__()[:27] == '<__main__.Spam object at 0x'
spam_hash = spam.__hash__()
assert type(spam_hash) == int
assert 8 * (10 ** 12) < spam_hash < 10 ** 13  # seems to always be a 13-digit number starting with an 8

assert spam.__class__ == Spam
assert str(Spam) == "<class '__main__.Spam'>"
assert Spam.__name__ == 'Spam'
