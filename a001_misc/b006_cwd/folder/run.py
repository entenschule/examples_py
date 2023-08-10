import os


assert __name__ == '__main__'

print('■', __file__)
print('●', os.getcwd())


try:
    os.mkdir('DELETE_ME')
except FileExistsError:
    pass

