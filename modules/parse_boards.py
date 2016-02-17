'''
This file includes a set of functions which can parse the boards info parsed from pinterest.com. These boards info will
be saved under data directory.
'''

import re

def parse_boards(lis):
    '''
    split the urls and parse the latter substring
    :param lis: list
    :return: lis
    '''
    outlis = []
    for url in lis:
        outlis.append(re.split("com",url))
    return outlis
