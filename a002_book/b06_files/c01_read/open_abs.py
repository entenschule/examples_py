import os

"""
works:
python -m a002_book.b06_files.c01_read.open_abs

works:
python a002_book/b06_files/c01_read/open_abs.py

fails:
cd a002_book/b06_files/c01_read
python open_abs.py
"""

folder_path = os.path.dirname(__file__)
file_path = folder_path + '/arab_roman.txt'
fobj = open(file_path, 'r')

for line in fobj:
    print(line)
fobj.close()