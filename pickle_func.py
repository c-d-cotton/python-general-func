#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')


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

