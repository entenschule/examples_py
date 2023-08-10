This script prints ■ `__file__` and ● `os.getcwd()`,
and does `os.mkdir('DELETE_ME')`.<br>
The folder is always created in the current working directory shown with `os.getcwd()`.

## with m-switch

### click

`python -m a001_misc.b006_cwd.folder.run`

``` 
/home/tilman/learn_py/examples_py/venv/bin/python -m a001_misc.b006_cwd.folder.run 
■ /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder/run.py
● /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder
```

#### try to run full command here

``` 
(venv) tilman@t570:~/learn_py/examples_py$ cd a001_misc/b006_cwd/folder
(venv) tilman@t570:~/learn_py/examples_py/a001_misc/b006_cwd/folder$ python -m a001_misc.b006_cwd.folder.run
/home/tilman/learn_py/examples_py/venv/bin/python: Error while finding module specification for 'a001_misc.b006_cwd.folder.run' (ModuleNotFoundError: No module named 'a001_misc')
```

### here

``` 
(venv) tilman@t570:~/learn_py/examples_py$ cd a001_misc/b006_cwd/folder
(venv) tilman@t570:~/learn_py/examples_py/a001_misc/b006_cwd/folder$ python -m run
■ /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder/run.py
● /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder
```

### parent

``` 
(venv) tilman@t570:~/learn_py/examples_py$ cd a001_misc/b006_cwd
(venv) tilman@t570:~/learn_py/examples_py/a001_misc/b006_cwd$ python -m folder.run
■ /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder/run.py
● /home/tilman/learn_py/examples_py/a001_misc/b006_cwd
```

### root

``` 
(venv) tilman@t570:~/learn_py/examples_py$ python -m a001_misc.b006_cwd.folder.run
■ /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder/run.py
● /home/tilman/learn_py/examples_py
```


## without m-switch

### click

`python run.py`

``` 
/home/tilman/learn_py/examples_py/venv/bin/python run.py 
■ run.py
● /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder
```

### here

``` 
(venv) tilman@t570:~/learn_py/examples_py$ cd a001_misc/b006_cwd/folder
(venv) tilman@t570:~/learn_py/examples_py/a001_misc/b006_cwd/folder$ python run.py 
■ run.py
● /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder
```

### parent

``` 
(venv) tilman@t570:~/learn_py/examples_py$ cd a001_misc/b006_cwd
(venv) tilman@t570:~/learn_py/examples_py/a001_misc/b006_cwd$ python folder/run.py 
■ folder/run.py
● /home/tilman/learn_py/examples_py/a001_misc/b006_cwd
```

### root

``` 
(venv) tilman@t570:~/learn_py/examples_py$ python a001_misc/b006_cwd/folder/run.py
■ a001_misc/b006_cwd/folder/run.py
● /home/tilman/learn_py/examples_py
```
