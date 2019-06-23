# tl/utils/ready.py
#
#

""" helper functions to display set options when bot is ready. """

## basic imports

import logging

## defines

defaultexclude = ["password", "issaved", "owner", "createdfrom", "cfile", "userid"]

## dogreeting function

def dogreeting(type, opts, cfg, how=None, exclude=[]):
    from tl.utils.log import getlevel
    level = getlevel(opts.loglevel or cfg.loglevel or "warn")
    if type == "console" and level == logging.ERROR: return
    if type == "console" and not opts.loglevel: how = how or "print"
    if not how: how = "log"
    for txt in greetingdata(opts, cfg, exclude):
        if how == "print": print(txt)
        elif how == "log": logging.log(level, txt)
        else: print(txt) ; logging.log(level, txt)

## greetingdata function

def greetingdata(opts, cfg, exclude=[]):
    exclude = defaultexclude + exclude
    result = []
    setops = setcfg = []
    if opts: setopts = ["%s (%s)" % (x, getattr(opts,x)) for x in opts.itemslist if x and x not in exclude and getattr(opts, x)]
    if cfg: setcfg = [ "%s (%s)" % (x.upper(), str(cfg[x])) for x in cfg if x and cfg[x] and x not in exclude and not x.startswith("_")]
    if setopts:
        result = ["O P T I O N S", " "]
        for txt in setopts: result.append("    %s" % txt)
        result.append(" ")
    result.append("C O N F I G")
    result.append(" ")
    for txt in setcfg: result.append("    %s" % txt)
    result.append(" ")
    return result
