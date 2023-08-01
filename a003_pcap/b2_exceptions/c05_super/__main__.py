"""
python -m a003_pcap.b2_exceptions.c05_super
"""


class SpamException(Exception):

    def __init__(self, message):

        assert self.args == super().args == (message,)

        super().__init__(self, message)

        assert self.args == super().args == (self, message)

        self.message = message


try:
    raise SpamException('■')
except SpamException as e:
    assert len(e.args) == 2
    arg_self, arg_message = e.args
    assert e == arg_self
    print(arg_self)
    print(arg_message)
