"""
python -m a003_pcap.b3_strings.c03_slice
"""


s = '0123456789'

slice_to_result = {
    s: [(None, None, None), (0, 10, 1)],
    '012345678': [(None, 9, None), (None, -1, None), (0, 9, 1), (0, -1, 1)],
    '02468': [(None, None, 2)],
    '0246': [(None, -2, 2)],
    '2468': [(2, None, 2)],
    '9876543210': [(None, None, -1), (-1, -11, -1)],
    '97531': [(None, None, -2)],
    '8642': [(8, 1, -2), (-2, -9, -2)]
}


for slice_result, slice_tuples in slice_to_result.items():
    for slice_tuple in slice_tuples:
        slice_object = slice(*slice_tuple)
        assert s[slice_object] == slice_result
