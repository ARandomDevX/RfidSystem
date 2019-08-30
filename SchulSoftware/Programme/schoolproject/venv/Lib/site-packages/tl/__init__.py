# tl/__init__.py
#
#

""" The new world. """

## basic imports

import logging
import imp
import sys

#### FIRST THE IMPORT STUFF

## _import function

def _import(name):
    """ do a import (full). """
    if not name: raise Exception(name)
    logging.info("importing %s" % name)
    res = __import__(name)
    return sys.modules[name]

## silent_import

def silent_import(name):
    from tl.utils.exception import exceptionmsg
    try: return _import(name)
    except Exception as ex: logging.error(exceptionmsg())

## force_import function

def force_import(name):
    """ force import of module <name> by replacing it in sys.modules. """
    try: del sys.modules[name]
    except KeyError: pass
    plug = _import(name)
    return plug

## import_byfile

def import_byfile(modname, filename):
    logging.info("importing %s" % filename)
    try: return imp.load_source(modname, filename)
    except NotImplementedError: return _import(filename[:-3].replace(os.sep, "."))

#### BASIC TYPES

## O class 

class O(object):

    __store__ = {}

    def __init__(self, *args, **kwargs):
        object.__init__(self)

## Event class

class Event(O):

    def __init__(self, *args, **kwargs):
        O.__init__(self)

## Bot class

class Bot(O): pass

## Driver class

class Driver(O): pass

