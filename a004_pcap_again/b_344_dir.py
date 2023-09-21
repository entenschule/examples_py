import math
import platform


default_dir = dir()
print(default_dir)

print('\n###############################################\n')

math_dir = dir(math)
print('only math:\n', [_ for _ in math_dir if _ not in default_dir])
print('\nmath and default:\n', [_ for _ in math_dir if _ in default_dir])
print('\nonly default:\n', [_ for _ in default_dir if _ not in math_dir])

print('\n###############################################\n')

platform_dir = dir(platform)
print('only platform:\n', [_ for _ in platform_dir if _ not in default_dir])
print('\nplatform and default:\n', [_ for _ in platform_dir if _ in default_dir])
print('\nonly default:\n', [_ for _ in default_dir if _ not in platform_dir])
