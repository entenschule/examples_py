"""
python -m a003_pcap.b3_strings.c02_find
"""


haystack = 'Spam Ham Panama'
needle = 'am'

########################################################################################################################

for i in range(20):
    place = haystack.find(needle, i)

    if i <= 12:
        assert haystack.index(needle, i) == place

    if i <= 2:
        assert place == 2
    elif 3 <= i <= 6:
        assert place == 6
    elif 7 <= i <= 12:
        assert place == 12
    else:  # i >= 13
        assert place == -1  # not found

########################################################################################################################

for i in range(20):
    place = haystack.rfind(needle, 0, i)
    if i >= 14:
        assert place == 12
    elif 8 <= i <= 13:
        assert place == 6
    elif 4 <= i <= 7:
        assert place == 2
    else:  # i <= 3
        assert place == -1  # not found
