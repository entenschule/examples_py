# change class variable

The main class in this example is `Bodyguard`.<br>
Its class variable is the list `protect`, which by default contains the king.<br>
The effects of changing `Bodyguard.protect` are not easily guessed.

Stackoverflow: [What is the logic of changing class variables?](https://stackoverflow.com/questions/76823174)


## main class with slightly different init methods

The four files contain the same classes and example variables.<br>
But there are small differences in `Bodyguard.__init__`,<br>
affecting whether an old object is modified, or a new one created.<br>

### reassign (better)

[reassign_better.py](reassign_better.py) behaves the way it should.

```python
class Bodyguard:
    protect = ['the king']

    def __init__(self, *args):
        self.protect = self.protect[:]  # force reassign also for generic guards
        if args:
            self.protect = self.protect + list(args)
```

### reassign (good, or rather not too bad)

[reassign_good.py](reassign_good.py) shows unwanted behavior for generic guards.

```python
    def __init__(self, *args):
        if args:
            self.protect = self.protect + list(args)
```

### add assign (bad)

The results in [addassign_bad.py](addassign_bad.py) make no sense.

```python
        if args:
            self.protect += list(args)
```

### append (bad)

Those in [append_bad.py](append_bad.py) neither. &nbsp;
(All variables in the same section have the same `protect`.)

```python
        if args:
            for arg in args:
                self.protect.append(arg)
```

(One _could_ probably try to understand the difference between the bad versions... Oh, look! A bird!)
