#!/usr/bin/env python3
"""
I'd also like to write a simple class to write lists in a similar manner to how I yield splits here.
Could use in createindex.

Basic idea:
    - Init function for class opens file.
    - append function too add an element and write to file if large enough.
    - close to write last elements and close file.

"""
# PYTHON_PREAMBLE_START_STANDARD:{{{

# Christopher David Cotton (c)
# http://www.cdcotton.com

# modules needed for preamble
import importlib
import os
from pathlib import Path
import sys

# Get full real filename
__fullrealfile__ = os.path.abspath(__file__)

# Function to get git directory containing this file
def getprojectdir(filename):
    curlevel = filename
    while curlevel is not '/':
        curlevel = os.path.dirname(curlevel)
        if os.path.exists(curlevel + '/.git/'):
            return(curlevel + '/')
    return(None)

# Directory of project
__projectdir__ = Path(getprojectdir(__fullrealfile__))

# Function to call functions from files by their absolute path.
# Imports modules if they've not already been imported
# First argument is filename, second is function name, third is dictionary containing loaded modules.
modulesdict = {}
def importattr(modulefilename, func, modulesdict = modulesdict):
    # get modulefilename as string to prevent problems in <= python3.5 with pathlib -> os
    modulefilename = str(modulefilename)
    # if function in this file
    if modulefilename == __fullrealfile__:
        return(eval(func))
    else:
        # add file to moduledict if not there already
        if modulefilename not in modulesdict:
            # check filename exists
            if not os.path.isfile(modulefilename):
                raise Exception('Module not exists: ' + modulefilename + '. Function: ' + func + '. Filename called from: ' + __fullrealfile__ + '.')
            # add directory to path
            sys.path.append(os.path.dirname(modulefilename))
            # actually add module to moduledict
            modulesdict[modulefilename] = importlib.import_module(''.join(os.path.basename(modulefilename).split('.')[: -1]))

        # get the actual function from the file and return it
        return(getattr(modulesdict[modulefilename], func))

# PYTHON_PREAMBLE_END:}}}

def yieldsplitfromchunks(filename, maxbytes=2000000000, encoding='UTF-8', split = '\n', removelastnewline = False, gzipfile = False):
    """
    Read chunks and split them into lines as I go. Advantage over read whole file is doesn't exceed memory capacity. Advantage over read line by line is doesn't require too many disk readings.

    USAGE:
    for line in importattr(__projectdir__ / Path('large.py'), 'yieldsplitfromchunks')(wikifolder + 'redirect/current/csv/output.csv', maxbytes = 1000000000, encoding='latin-1'):
    """

    if gzipfile is True:
        import gzip
        fileopen = gzip.open(filename, 'rb')
    else:
        fileopen = open(filename, 'r', encoding = encoding)
        

    readingfile = True
    with fileopen as f:
        appendatstart = ''
        while readingfile:

            # read and decode if not already decoded
            if gzipfile is True:
                newtext = f.read(maxbytes).decode('latin-1')
            else:
                newtext = f.read(maxbytes)

            # add final part of lines from before
            lines = (appendatstart + newtext).split(split)

            if newtext == '':
                readingfile = False

                # since files end with \n, may be redundant line at end
                if split == '\n' and removelastnewline is True and lines[-1] == '':
                    lines.pop(-1)

            # appendatstart for next time
            if readingfile is True:
                appendatstart = lines.pop(-1)

            for line in lines:
                yield(line)

# for line in importattr(__projectdir__ / Path('large.py'), 'yieldsplitfromchunks')('hello.txt', maxbytes = 10000, encoding='latin-1', split = '\n\n\n\n'):
#     print(line)
#     print(1)
