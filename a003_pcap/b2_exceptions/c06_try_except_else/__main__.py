"""
python -m a003_pcap.b2_exceptions.c06_try_except_else
"""


x = 1

try:
    x = 2 / x
except ZeroDivisionError as e:
    print('■', e)
except Exception as e:
    print('◆', e)
else:
    x += 500

print(x)
