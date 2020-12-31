#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

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
