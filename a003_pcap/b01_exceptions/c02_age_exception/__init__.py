class AgeException(Exception):
    def __init__(self, age):
        parent_class = super(AgeException, self)
        parent_class.__init__(f'Something seems to be wrong with age {age}.')


try:
    raise AgeException(16)
except AgeException as e:
    print(e)
