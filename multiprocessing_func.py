#!/usr/bin/env python3
"""
When call function using importattr that uses multiprocessing, need to call with bybasename = True.
The function that multiprocessing is called upon should be given by its name rather than by using importattr.
"""
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

# Pooling Classes:{{{1
import multiprocessing
import multiprocessing.pool
class NoDaemonProcess(multiprocessing.Process):
    """
    Used to do pool of pool.
    See http://stackoverflow.com/questions/6974695/python-process-pool-non-daemonic
    Works by making 'daemon' attribute always return False
    """

    def _get_daemon(self):
        return False

    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)


class MyPool(multiprocessing.pool.Pool):
    """
    Used to do pool of pool.
    See NoDaemonProcess function
    """
    Process = NoDaemonProcess


