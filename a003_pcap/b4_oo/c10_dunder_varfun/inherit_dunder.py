class Liar:
    def __do(self):
        return 'tell lies'


class Killer:
    def __do(self):
        return 'kill people'


###################################


class Spy(Liar, Killer):
    pass


class Agent(Killer, Liar):
    pass


###################################


spy = Spy()
agent = Agent()

for person in [spy, agent]:
    assert person._Liar__do() == 'tell lies'
    assert person._Killer__do() == 'kill people'
