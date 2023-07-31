"""
python -m a003_pcap.b2_exceptions.c12_undefined_exception
"""


try:
    raise UndefinedException
except NameError:
    print('NameError')
except UndefinedException:
    print('UndefinedException')
except:
    pass


"""
The undefined exception does not cause problems beyond raising the NameError.
"""
