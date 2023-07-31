"""
python -m a003_pcap.b2_exceptions.c05_super
"""


short = True


class SpamException(Exception):

    def __init__(self, message):

        if short:
            super().__init__(self, message)
        else:
            super(SpamException, self).__init__(self, message)

        self.message = message


raise SpamException('■')
