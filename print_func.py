#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

def printorwrite(message, filename, printmessage = True, rewrite = False):
    if rewrite is True and os.path.isfile(filename):
        os.remove(filename)
    if filename is not None:
        with open(filename, 'a+') as f:
            f.write(str(message) + '\n')
    if printmessage is True:
        print(message)
