"""
python -m a003_pcap.b4_oo.c10_dunder_varfun.spy_simple
"""


class Driver:
    job = 'driver'


assert Driver.job == 'driver'

driver = Driver()
assert driver.job == 'driver'


########################################################################################################################


class Spy:
    __job = 'spy'
    __cover_job = 'trade commissioner'

    def job(self, password):
        return self.__job if password == 'secret' else self.__cover_job


try:
    Spy.__job
    assert False
except AttributeError as e:
    assert str(e) == "type object 'Spy' has no attribute '__job'"


assert Spy.job(Spy, 'secret') == 'spy'  # This is weird, but it works.


########################################################################################################################


spy = Spy()

try:
    spy.__job
    assert False
except AttributeError as e:
    assert str(e) == "'Spy' object has no attribute '__job'"


assert spy.job('secret') == 'spy'
assert spy.job('guess') == 'trade commissioner'


########################################################################################################################


# Surprise! Actually the double underscores don't hide anything.
# `__job` is accessible as `_Spy__job`. This is called name mangling.


assert spy._Spy__job == 'spy'
