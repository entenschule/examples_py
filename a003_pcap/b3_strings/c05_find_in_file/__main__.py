import os


"""
python -m a003_pcap.b3_strings.c05_find_in_file
"""


folder_path = os.path.dirname(__file__)
file_path = folder_path + '/breakfast.txt'


# fails #################################################

fobj = open(file_path, 'r')

found = 'eggs' in fobj
maybe_not = '' if found else 'not '
print(f'{maybe_not}found in TextIOWrapper')

fobj.close()


# works #################################################

fobj = open(file_path, 'r')

for line in fobj:
    found = 'eggs' in line
    maybe_not = '' if found else 'not '
    print(f'{maybe_not}found in line')

fobj.close()


"""
not found in TextIOWrapper
found in line
"""