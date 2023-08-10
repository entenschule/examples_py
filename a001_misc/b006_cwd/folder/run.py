import os
import sys


assert __name__ == '__main__'


project_folder = os.path.abspath(__file__ + '/../../../../')
maybe_not = 'NOT ' if project_folder not in sys.path else ''
triangle = '▷' if project_folder not in sys.path else '▶'

print('■', __file__)
print('●', os.getcwd())
print(triangle, f'{project_folder} is {maybe_not}in pythonpath.')


try:
    os.mkdir('DELETE_ME')
except FileExistsError:
    pass
