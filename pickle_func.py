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


def func_load(f1, filename, load = False, save = True, **kwargs):
    """
    Function to allow me to quickly load f1. Uses pickle if load is True.
    f1 needs to have the argument load as well since I call f1 with the argument load.
    I try to call f1 with argument load since if f1 calls another function f0 using func_load then I want to also pass load to that function.

    Always run the function by default.
    But if set load = True and pickled saved item exists then load instead.
    Always save item in pickled form when run function.
    """

    import os
    import pickle

    if os.path.isfile(filename) and load is True:
        with open(filename, 'rb') as f:
            item = pickle.load(f)
    else:
        try:
            item = f1(load = load, **kwargs)
        except TypeError:
            item = f1(**kwargs)
        # I may have saved the pickled item during the actual run of the function in which case this isn't necessary.
        if save is True:
            with open(filename, 'wb') as f:
                pickle.dump(item, f)

    return(item)

