#!/usr/bin/env python3
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

def issubpath(filename, superpath, trueifsame = True):
    """
    Checks whether filename is a subpath of superpath
    Would return true for issubpath('/home/user/1.txt', '/home/user/')
    False for isssubpath('/home/user2/1.txt', '/home/user/')
    If trueifsame then also return True for issubpath('/home/user/', '/home/user/')
    """
    filename = os.path.abspath(filename)
    superpath = os.path.abspath(superpath)
    if filename.startswith(superpath + os.sep) or (trueifsame is True and filename == superpath):
        return(True)
    else:
        return(False)


def md5Checksum(filePath):
    """
    Taken from https://www.joelverhagen.com/blog/2011/02/md5-hash-of-file-in-python/ on 20171226.
    """
    import hashlib
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


def twofilesaresame(filename1, filename2):
    checksum1 = md5Checksum(filename1)
    checksum2 = md5Checksum(filename2)

    if checksum1 == checksum2:
        return(True)
    else:
        return(False)
    
def deletelinksdirectory(folder):
    for root, dirs, files in os.walk(folder):
        for name in files:
            if os.path.islink(os.path.join(root, name)):
                os.unlink(os.path.join(root, name))
        for name in dirs:
            if os.path.islink(os.path.join(root, name)):
                os.unlink(os.path.join(root, name))
