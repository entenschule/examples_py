"""
python -m a003_pcap.b4_oo.c10_dunder_varfun.spy_extended
"""


class Spy:
    __job = 'spy'
    __cover_job = 'trade commissioner'
    __password_string = 'secret'

    def __password_function(self):
        return self.__password_string

    def job(self, password):
        correct_password = self.__password_function()
        return self.__job if password == correct_password else self.__cover_job

    def smalltalk(self):
        return 'patati patata'


assert Spy.smalltalk(Spy) == 'patati patata'

try:
    Spy.job(Spy, 'guess') == 'trade commissioner'
    assert False
except TypeError as e:
    assert str(e) == "__password_function() missing 1 required positional argument: 'self'"


try:
    Spy.__password_function()
    assert False
except AttributeError as e:
    assert str(e) == "type object 'Spy' has no attribute '__password_function'"


########################################################################################################################


spy = Spy()

assert spy.job('secret') == 'spy'
assert spy.job('guess') == 'trade commissioner'
assert spy.smalltalk() == 'patati patata'

try:
    spy.__password_function()
    assert False
except AttributeError as e:
    assert str(e) == "'Spy' object has no attribute '__password_function'"


########################################################################################################################


assert spy._Spy__job == 'spy'
assert spy._Spy__password_string == spy._Spy__password_function() == 'secret'
