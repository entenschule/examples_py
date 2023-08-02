# change class variable

The main class in this example is `Bodyguard`.<br>
Its class variable is the list `protect`, which by default contains the king.<br>
The effects of changing `Bodyguard.protect` are not easily guessed.


## main class with slightly different init methods

### redefine (good)

[redefine_good.py](redefine_good.py) is not without surprises, but gives meaningful results.

```python
class Bodyguard:
    protect = ['the king']

    def __init__(self, *args):
        if args:
            self.protect = self.protect + list(args)
```

### append (bad)

[append_bad.py](append_bad.py) contains the same classes, but with a (seemingly) small difference in `Bodyguard.__init__`.<br>
The example bodyguards are the same. The results are useless.

```python
class Bodyguard:
    protect = ['the king']

    def __init__(self, *args):
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
