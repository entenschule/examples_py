"""
fails:
python -m a002_book.b06_files.c01_read.open

fails:
python a002_book/b06_files/c01_read/open.py

works:
cd a002_book/b06_files/c01_read
python open.py
"""

fobj = open('arab_roman.txt', 'r')

for line in fobj:
    print(line)
fobj.close()
