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

import shutil

def chmodrecursive(folder, mode):
    """
    Mode takes format 0o777

    Also used in mysubmodules project.
    """
    import os

    if not os.path.islink(folder):
        if os.path.isdir(folder):
            os.chmod(folder, mode)
            for root, dirs, files in os.walk(folder):
                for d in dirs :
                    if not os.path.islink(os.path.join(root, d)):
                        os.chmod(os.path.join(root, d), mode)
                for f in files :
                    if not os.path.islink(os.path.join(root, f)):
                        os.chmod(os.path.join(root, f), mode)
        else:
            os.chmod(folder, mode)




def rmrecursive(folder):
    print(folder)
    if not os.path.islink(folder) and os.path.isdir(folder):
        chmodrecursive(folder, 0o755)

        # need to make folder containing thing to be deleted readable as well
        if folder.endswith('/') or folder.endswith('\\'):
            folder = folder[: -1]
        os.chmod(folder, 0o755)
        shutil.rmtree(folder)
    else:
        os.remove(folder)


