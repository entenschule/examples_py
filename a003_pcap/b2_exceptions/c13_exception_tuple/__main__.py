"""
python -m a003_pcap.b2_exceptions.c13_exception_tuple
"""


class SpamError(Exception):
    pass


class EggsError(Exception):
    pass


class NailsError(Exception):
    pass


class FoodError(SpamError, EggsError):
    pass


try:
    raise FoodError('Oh noooo!')
except (SpamError, EggsError, NailsError) as e:
    print(e)
