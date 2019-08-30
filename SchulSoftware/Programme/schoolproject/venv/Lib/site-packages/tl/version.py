# tl/version.py
#
#

""" version related stuff. """

## tl imports


## basic imports

import os
import binascii

## defines

version = "0.5"
__version__ = version

## getversion function

def getversion(txt=""):
    """ return a version string. """
    if txt: return "%s - %s" % (version, txt)
    else: return version

def getfullversion(txt="", repo=False):
    from tl.config import getmainconfig
    cfg = getmainconfig()
    options = cfg.display()
    tip = None
    if repo:
        try:
            from mercurial import context, hg, node, repo, ui
            repository = hg.repository(ui.ui(), '.')
            ctx = context.changectx(repository)
            tip = str(ctx.rev())
        except: tip = None
    if tip: options.append("HG " + tip)
    return "T I M E L I N E - %s - %s - %s" % (version, txt.upper(), ", ".join(options))
