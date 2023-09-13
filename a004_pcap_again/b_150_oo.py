class BaseDiner:
    def __init__(self):
        self.menu = None  # pointless, but appeases the IDE
        self.make_menu()

    def make_menu(self):
        self.menu = 'Spam'


class FancyDiner(BaseDiner):
    def __init__(self):
        super().__init__()

    def make_menu(self):
        self.menu = 'Eggs'


class SuperFancyDiner(BaseDiner):
    def __init__(self):
        base_diner = BaseDiner()
        self.base_menu = base_diner.menu
        super().__init__()

    def make_menu(self):
        self.menu = ' '.join([self.base_menu, 'Eggs'])


base_diner = BaseDiner()
fancy_diner = FancyDiner()
super_fancy_diner = SuperFancyDiner()


assert base_diner.menu == 'Spam'
assert fancy_diner.menu == 'Eggs'
assert super_fancy_diner.menu == 'Spam Eggs'


"""
Without the `self.spam = None` PyCharm will make this complaint:
Instance attribute spam defined outside __init__ 
"""
