import os

"""
works:
python -m a002_book.b06_files.c01_read.with_abs

works:
python a002_book/b06_files/c01_read/with_abs.py

fails:
cd a002_book/b06_files/c01_read
python with_abs.py
"""

folder_path = os.path.dirname(__file__)
file_path = folder_path + '/arab_roman.txt'

dictionary = dict()

with open(file_path, 'r') as fobj:
    for line in fobj:
        line = line.strip()
        a, b = line.split(' ')
        dictionary[int(a)] = b
    fobj.close()

print(dictionary)
