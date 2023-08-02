# change class variable

The main class in this example is `Bodyguard`.<br>
Its class variable is the list `protect`, which by default contains the king.<br>
The effects of changing `Bodyguard.protect` are not easily guessed.


## main class with slightly different init methods

The three files contain the same classes and example variables.<br>
But there is a (seemingly) small difference in `Bodyguard.__init__`.<br>
The results for `+=` and `append` make no sense at all. (But they are different.)

### reassign (good)

[reassign_good.py](reassign_good.py) is not without surprises, but gives meaningful results.

```python
class Bodyguard:
    protect = ['the king']

    def __init__(self, *args):
        if args:
            self.protect = self.protect + list(args)
```

### add assign (bad)

[addassign_bad.py](addassign_bad.py) &nbsp;
(The first specific guards `bg_prime` and `bg_foobar` have the same `protect` in all sections.)

```python
        if args:
            self.protect += list(args)
```

### append (bad)

[append_bad.py](append_bad.py) &nbsp;
(All variables in the same section have the same `protect`.)

```python
        if args:
            for arg in args:
                self.protect.append(arg)
```

## different classes to change the class variable

### change in definition of subclass

```python
class AnnoyingBodyguard(Bodyguard):
    Bodyguard.protect = ['his majesty the king']
```

### change in init of unrelated class

```python
class Bureaucrat:
    def __init__(self, name):
        Bodyguard.protect.append(name)
```
