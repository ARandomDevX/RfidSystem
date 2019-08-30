# tl/utils/creds.py
#
#

""" credentials helper funcions. """

# tl feedback

from tl.datadir import getdatadir
from tl.errors import RequireError
from tl import import_byfile

## basic imports

import os
import logging

## getcredsfile function

def getcredsmod(datadir=None, doraise=False):
    """ returnd credendtials.py as a module. """
    if not datadir: datadir = getdatadir()
    try:
        mod = import_byfile("credentials", datadir + os.sep + "config" + os.sep + "credentials.py")
        global go
        go = True
    except (IOError, ImportError):
        if doraise: raise RequireError("creds needed (%s/config/credentials.py)" % datadir)
        else: logging.warn("creds needed (%s/config/credentials.py)" % datadir) 
        return
    logging.error("creds found credentials for %s" % str(mod))
    return mod
