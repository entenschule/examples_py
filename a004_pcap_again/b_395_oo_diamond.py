class Foo:
    value = "f o o"


class Spam(Foo):
    value = "s p a m"


class Eggs(Foo):
    pass


old_eggs_id = id(Eggs)


class Fish(Eggs, Spam):
    pass


old_fish_id = id(Fish)


assert [base.__name__ for base in Fish.__bases__] == ['Eggs', 'Spam']


# `value` is only an inherited attribute of `Eggs`.
assert hasattr(Eggs, 'value')
assert 'value' not in Eggs.__dict__

# `value` is a direct attribute of `Spam`.
assert hasattr(Spam, 'value')
assert 'value' in Spam.__dict__


# `Fish` inherits `value` from the second argument `Spam`, because directness outranks argument order.
assert Fish.value == Fish().value == 's p a m'


# redeclare to set own `value`
class Eggs(Foo):
    value = 'e g g s'


assert id(Eggs) != old_eggs_id   # `Eggs` was changed.
assert id(Fish) == old_fish_id   # But `Fish` does not care.

# Nothing changed, because `Fish` still inherits from the old `Eggs`.
assert Fish.value == Fish().value == 's p a m'


# redeclare to make `Fish` use the new `Eggs`
class Fish(Eggs, Spam):
    pass


assert id(Fish) != old_fish_id  # `Fish was changed.


# Now both `Eggs` and `Spam` have `value`. So the child inherits from the old argument.
assert Fish.value == Fish().value == 'e g g s'
