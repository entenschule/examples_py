This script prints ■ `__file__` and ● `os.getcwd()`,
and does `os.mkdir('DELETE_ME')`.<br>
Additionally it prints, ▶ whether or not `examples_py` is in `sys.path`.<br>
The folder is always created in the current working directory shown with `os.getcwd()`.

Stackoverflow:
[What is the console equivalent of clicking on a command in a markdown file in PyCharm?](https://stackoverflow.com/questions/76876104)<br>
**Trying to rephrase the answer:**<br>
The clickable command should be `python -m run`. That also works from the console in `folder`.<br>
The long version also works with the click, because PyCharm has added `examples_py` to pythonpath.<br>
Without the help of PyCharm that is not the case. Therefore, the long command fails from `folder` in the console.

## with m-switch

### click

`python -m a001_misc.b006_cwd.folder.run`<br>
`python -m run`

``` 
/home/tilman/learn_py/examples_py/venv/bin/python -m run 
■ /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder/run.py
● /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder
▶ /home/tilman/learn_py/examples_py is in pythonpath.
```

#### same command fails in console

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
▷ /home/tilman/learn_py/examples_py is NOT in pythonpath.
```

### root

``` 
(venv) tilman@t570:~/learn_py/examples_py$ python -m a001_misc.b006_cwd.folder.run
■ /home/tilman/learn_py/examples_py/a001_misc/b006_cwd/folder/run.py
● /home/tilman/learn_py/examples_py
▶ /home/tilman/learn_py/examples_py is in pythonpath.
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
▷ /home/tilman/learn_py/examples_py is NOT in pythonpath.
```

### root

``` 
■ a001_misc/b006_cwd/folder/run.py
● /home/tilman/learn_py/examples_py
▷ /home/tilman/learn_py/examples_py is NOT in pythonpath.
```
