#!/usr/bin/env python3
"""
I'd also like to write a simple class to write lists in a similar manner to how I yield splits here.
Could use in createindex.

Basic idea:
    - Init function for class opens file.
    - append function too add an element and write to file if large enough.
    - close to write last elements and close file.

"""
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

def yieldsplitfromchunks(filename, maxbytes=2000000000, encoding='UTF-8', split = '\n', removelastnewline = False, gzipfile = False):
    """
    Read chunks and split them into lines as I go. Advantage over read whole file is doesn't exceed memory capacity. Advantage over read line by line is doesn't require too many disk readings.

    USAGE:
    for line in yieldsplitfromchunks(wikifolder + 'redirect/current/csv/output.csv', maxbytes = 1000000000, encoding='latin-1'):
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

# for line in yieldsplitfromchunks('hello.txt', maxbytes = 10000, encoding='latin-1', split = '\n\n\n\n'):
#     print(line)
#     print(1)
