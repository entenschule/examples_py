f = open("data_file", "w")

f.write('ABC\nDEF\nUVW\nXYZ')  # no newline at end of file

try:
    f.readline()
    assert False  # canary
except IOError as e:
    assert str(e) == 'not readable'

f.close()

#######################################################################

f = open("data_file", "r")

try:
    f.write('Read only? Not for me!')
    assert False  # canary
except IOError as e:
    assert str(e) == 'not writable'

assert f.readline() == 'ABC\n'
assert f.readline() == 'DEF\n'

remaining_lines = ['UVW\n', 'XYZ']  # no newline at end of file

for i, line in enumerate(f.readlines()):
    assert line == remaining_lines[i]

f.close()

#######################################################################

f = open("data_file", "r")
assert f.readline() == 'ABC\n'  # content as before
f.close()

# write empty file
f = open("data_file", "w")
f.close()

f = open("data_file", "r")
assert f.readline() == ''  # no content
f.close()
