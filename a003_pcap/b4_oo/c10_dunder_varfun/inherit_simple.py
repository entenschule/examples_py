class Liar:
    def do(self):
        return 'tell lies'


class Killer:
    def do(self):
        return 'kill people'


###################################


class Spy(Liar, Killer):
    pass


class Agent(Killer, Liar):
    pass


###################################


spy = Spy()
agent = Agent()

assert spy.do() == 'tell lies'
assert agent.do() == 'kill people'
