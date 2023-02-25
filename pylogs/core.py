# Custom log levels for Python's logging module.
#
# Modder: ReiDoBrega
# Last Change: December 11, 2022

"""
Custom log levels for Python's :mod:`logging` module.
"""

import logging
import sys
from typing import NoReturn
from .defaults import NOTICE, SPAM, SUCCESS, VERBOSE, LOGKEY


def install():
    """
    Make :class:`Logger` the default logger class.

    The :func:`install()` function uses :func:`~logging.setLoggerClass()` to
    configure :class:`Logger` as the default class for all loggers
    created by :func:`logging.getLogger()` after :func:`install()` has been
    called. Here's how it works:

    .. code-block:: python

        import logging
        import pylogs

        pylogs.install()
        logger = logging.getLogger(__name__) # will be a Logger instance
    """
    logging.setLoggerClass(Logger)


def addLogLevel(value, name):
    """
    Add a new log level to the :mod:`logging` module.

    :param value: The log level's number (an integer).
    :param name: The name for the log level (a string).
    """
    logging.addLevelName(value, name)
    setattr(logging, name, value)


# Define the NOTICE log level.
addLogLevel(NOTICE, 'NOTICE')

# Define the SPAM log level.
addLogLevel(SPAM, 'SPAM')

# Define the SUCCESS log level.
addLogLevel(SUCCESS, 'SUCCESS')

# Define the VERBOSE log level.
addLogLevel(VERBOSE, 'VERBOSE')

# Define the LOGKEY log level.
# Yeah old NFTool users, you know this..
addLogLevel(LOGKEY, 'LOGKEY')


class Logger(logging.Logger):

    """
    Custom logger class to support the additional logging levels.

    This subclass of :class:`logging.Logger` adds support for the additional
    logging methods :func:`notice()`, :func:`spam()`, :func:`success()`, 
    :func:`verbose()`, :func:`logkey()`, and :func:`exit()`.

    You can use :func:`pylogs.install()` to make :class:`Logger`
    the default logger class.
    """

    def __init__(self, *args, **kw):
        """
        Initialize a :class:`Logger` object.

        :param args: Refer to the superclass (:class:`logging.Logger`).
        :param kw: Refer to the superclass (:class:`logging.Logger`).

        This method first initializes the superclass and then it sets the root
        logger as the parent of this logger.

        The function :func:`logging.getLogger()` is normally responsible for
        defining the hierarchy of logger objects however because verbose
        loggers can be created by calling the :class:`Logger`
        constructor, we're responsible for defining the parent relationship
        ourselves.
        """
        logging.Logger.__init__(self, *args, **kw)
        self.parent = logging.getLogger()

    def notice(self, msg, *args, **kw):
        """Log a message with level :data:`NOTICE`. The arguments are interpreted as for :func:`logging.debug()`."""
        if self.isEnabledFor(NOTICE):
            self._log(NOTICE, msg, args, **kw)

    def spam(self, msg, *args, **kw):
        """Log a message with level :data:`SPAM`. The arguments are interpreted as for :func:`logging.debug()`."""
        if self.isEnabledFor(SPAM):
            self._log(SPAM, msg, args, **kw)

    def success(self, msg, *args, **kw):
        """Log a message with level :data:`SUCCESS`. The arguments are interpreted as for :func:`logging.debug()`."""
        if self.isEnabledFor(SUCCESS):
            self._log(SUCCESS, msg, args, **kw)

    def verbose(self, msg, *args, **kw):
        """Log a message with level :data:`VERBOSE`. The arguments are interpreted as for :func:`logging.debug()`."""
        if self.isEnabledFor(VERBOSE):
            self._log(VERBOSE, msg, args, **kw)

    def logkey(self, message, *args, **kws):
        """Log a message with level :data:`LOGKEY`. The arguments are interpreted as for :func:`logging.debug()`."""
        if self.isEnabledFor(LOGKEY):
            self._log(LOGKEY, message, args, **kws)

    def exit(self, msg, *args, **kwargs) -> NoReturn:
        """
        Log 'msg % args' with severity 'CRITICAL' and terminate the program
        with a default exit code of 1.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.exit("Houston, we have a %s", "major disaster", exc_info=1)
        """
        self.critical(msg, *args, **kwargs)
        sys.exit(1)