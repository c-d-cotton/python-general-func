#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/../')

def f1(hello = 'hello', goodbye = ''):
    print('Running f1!')
    return(hello + goodbye)

def f1_load(load = False, **kwargs):
    sys.path.append(str(__projectdir__))
    from pickle_func import func_load
    ret = func_load(f1, '1.pickle', load = load, **kwargs)

    return(ret)

# Run:{{{1
print(f1_load(load = False, hello = 'hell2o', goodbye = 'goodbye'))
# even though changed optional arguments, still load old version
print(f1_load(load = True, hello = 'wow'))
# now should rerun function and get different argument
print(f1_load(load = False, hello = 'wow'))
