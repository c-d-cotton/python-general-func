#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

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


