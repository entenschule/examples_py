# change class variable

The main class in this example is `Bodyguard`.<br>
Its class variable is the list `protectees`, which by default contains the king.<br>
The effects of changing `Bodyguard.protectees` are not easily guessed.


## main class with slightly different init methods

### redefine (good)

[redefine_good.py](redefine_good.py) is not without surprises, but gives meaningful results.

```python
class Bodyguard:
    protectees = ['the king']

    def __init__(self, *args):
        if args:
            self.protectees = self.protectees + list(args)
```

### append (bad)

[append_bad.py](append_bad.py) differs only in the init method of the main class. The results are useless.

```python
class Bodyguard:
    protectees = ['the king']

    def __init__(self, *args):
        if args:
            for arg in args:
                self.protectees.append(arg)
```


## different classes to change the class variable

### change in definition of subclass

```python
class AnnoyingBodyguard(Bodyguard):
    Bodyguard.protectees = ['his majesty the king']
```

### change in init of unrelated class

```python
class Bureaucrat:
    def __init__(self, name):
        self.name = name
        Bodyguard.protectees.append(name)
```
