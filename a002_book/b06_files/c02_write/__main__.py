import os

"""
python -m a002_book.b06_files.c02_write
"""

words = {
    'Germany': 'Deutschland',
    'Spain': 'Spanien',
    'Greece': 'Griechenland'
}

folder_path = os.path.dirname(__file__)
file_path = folder_path + '/output.txt'

with open(file_path, 'w') as fobj:
    for engl in words:
        fobj.write(f'{engl} {words[engl]}\n')
