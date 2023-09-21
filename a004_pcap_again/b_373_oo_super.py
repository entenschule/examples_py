class Parent:
    def __init__(self):
        self.given_name = 'John'
        self.family_name = 'Doe'

    def name(self):
        return self.given_name + ' ' + self.family_name


class A(Parent):
    def __init__(self):
        super().__init__()  # without argument
        self.given_name = 'Alfred'


class B(Parent):
    def __init__(self):
        Parent.__init__(self)  # with argument
        self.given_name = 'Berta'


assert Parent().name() == 'John Doe'
assert A().name() == 'Alfred Doe'
assert B().name() == 'Berta Doe'
