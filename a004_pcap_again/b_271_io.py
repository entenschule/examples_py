ba = bytearray(3)

assert ba == b'\x00\x00\x00'
assert len(ba) == 3
assert ba[0] == 0

ba[0] = 128
ba[2] = 255

assert ba == b'\x80\x00\xff'

try:
    ba[0] = 256
    assert False  # canary
except ValueError as e:
    assert str(e) == 'byte must be in range(0, 256)'
