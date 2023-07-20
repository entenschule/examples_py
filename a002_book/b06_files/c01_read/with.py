"""
fails:
python -m a002_book.b06_files.c01_read.with

fails:
python a002_book/b06_files/c01_read/with.py

works:
cd a002_book/b06_files/c01_read
python with.py
"""

with open('arab_roman.txt', 'r') as fobj:
    for line in fobj:
        print(line)
    fobj.close()
