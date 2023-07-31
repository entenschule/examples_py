import platform


"""
python -m a003_pcap.b1_modpack.c01_platform
"""


code_strings = [
    'system()',  # Linux
    'platform()',  # Linux-5.15.0-76-generic-x86_64-with-glibc2.29
    'platform(aliased=True, terse=True)',  # as above
    'version()',  # #83~20.04.1-Ubuntu SMP Wed Jun 21 20:23:31 UTC 2023

    'processor()',  # x86_64
    'machine()',  # x86_64

    'python_version_tuple()',  # ('3', '8', '10')
    'python_implementation()',  # 'CPython'
]


for code_string in code_strings:
    print(code_string, '  ', eval('platform.' + code_string))
