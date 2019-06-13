# tl/exit.py
#
#

""" tl's finaliser """

## tl imports

from .utils.exception import handle_exception
from .utils.locking import globallocked
from .utils.trace import whichmodule
from .persist import cleanup
from .runner import allrunners

## basic imports

import atexit
import os
import time
import sys
import logging

## functions

@globallocked
def globalshutdown(exit=True):
    """ shutdown the bot. """
    try:
        try: sys.stdout.write("\n")
        except: pass
        txt = "SHUTTING DOWN (%s)" % time.ctime(time.time())
        logging.error(txt)
        from .fleet import getfleet
        fleet = getfleet()
        logging.warn('shutting down fleet')
        fleet.exit()
        logging.warn('shutting down plugins')
        from tl.plugins import plugs
        plugs.exit()
        logging.warn("shutting down runners")
        for runner in allrunners:
            try: runner.stop()
            except: handle_exception()
        logging.warn("cleaning up any open files")
        while cleanup(): time.sleep(1)
        try: os.remove('tl.pid')
        except: pass
        from .utils.url import stats
        nr = stats.get("urlnotenabled")
        if nr: logging.error("%s UrlNotEnabled catched" % nr)
        print("")
        logging.warn('done')
        sys.stdout.flush()
        if exit: os._exit(0)
    except Exception as ex:
        handle_exception()
        logging.critical(str(ex))
        if exit: os._exit(1)
