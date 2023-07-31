"""
python -m a003_pcap.b2_exceptions.c02_try_finally_continue
"""


for i in range(3):
    print('----------------', i)
    try:
        print('try')
        quotient = 1 / i
        print(f'● quotient: {quotient}')
    finally:
        print('finally')
        continue
