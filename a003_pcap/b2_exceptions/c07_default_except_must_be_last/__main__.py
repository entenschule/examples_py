"""
python -m a003_pcap.b2_exceptions.c07_default_except_must_be_last
"""


try:
    raise Exception
# except:
#     print('EMPTY')
except BaseException:
    print('BaseException')
except Exception:
    print('Exception')
except ValueError:
    print('ValueError')
