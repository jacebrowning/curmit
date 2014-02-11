#!/usr/bin/env python

"""
Grabs text from a URL and commits it.
"""

import os
import sys
import argparse
import logging
from pkg_resources import get_distribution, DistributionNotFound

__project__ = 'curmit'
__version__ = None  # required for initial installation
try:
    __version__ = get_distribution(__project__).version  # pylint: disable=E1103
except DistributionNotFound:  # pragma: no cover, manual test
    VERSION = __project__ + '-' + '(local)'
else:
    VERSION = __project__ + '-' + __version__
CLI = __project__


# Logging settings
DEFAULT_LOGGING_FORMAT = "%(message)s"
VERBOSE_LOGGING_FORMAT = "%(levelname)s: %(message)s"
VERBOSE2_LOGGING_FORMAT = "%(levelname)s: %(module)s:%(lineno)d: %(message)s"
DEFAULT_LOGGING_LEVEL = logging.WARNING
VERBOSE_LOGGING_LEVEL = logging.INFO
VERBOSE2_LOGGING_LEVEL = logging.DEBUG


class HelpFormatter(argparse.HelpFormatter):
    """Command-line help text formatter with wider help text."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, max_help_position=40, **kwargs)


class WarningFormatter(logging.Formatter, object):
    """Logging formatter that always displays a verbose logging
    format for logging level WARNING or higher."""

    def __init__(self, default_format, verbose_format, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_format = default_format
        self.verbose_format = verbose_format

    def format(self, record):
        """Python 3 hack to change the formatting style dynamically."""
        if record.levelno > logging.INFO:
            self._style._fmt = self.verbose_format  # pylint: disable=W0212
        else:
            self._style._fmt = self.default_format  # pylint: disable=W0212
        return super().format(record)

# Shared command-line arguments
DEBUG = argparse.ArgumentParser(add_help=False)
DEBUG.add_argument('-V', '--version', action='version', version=VERSION)
DEBUG.add_argument('-v', '--verbose', action='count', default=0,
                   help="enable verbose logging")
SHARED = {'formatter_class': HelpFormatter, 'parents': [DEBUG]}


def main(args=None):
    """Process command-line arguments and run the program."""

    # Main parser
    parser = argparse.ArgumentParser(prog=CLI, description=__doc__, **SHARED)
    parser.add_argument('-g', '--gui', action='store_true',
                        help="launch the GUI")
    parser.add_argument('-d', '--daemon', action='store_true',
                        help="if terminal mode, run forever")
    parser.add_argument('-q', '--no-log', action='store_true',
                        help="do not create a log for downloads")
    # TODO: support sharing multiple songs
    parser.add_argument('-s', '--share', metavar='PATH',
                        help="recommend a song")
    parser.add_argument('-i', '--incoming', action='store_true',
                        help="display the incoming songs")
    parser.add_argument('-o', '--outgoing', action='store_true',
                        help="display the outgoing songs")
    parser.add_argument('-u', '--users', metavar='n', nargs='*',
                        help="filter to the specified usernames")
    parser.add_argument('-n', '--new', metavar='FirstLast',
                        help="create a new user")
    parser.add_argument('-x', '--delete', action='store_true',
                        help="delete the current user")
    # Hidden argument to override the root sharing directory path
    parser.add_argument('--root', metavar="PATH", help=argparse.SUPPRESS)
    # Hidden argument to run the program as a different user
    parser.add_argument('--test', metavar='FirstLast', help=argparse.SUPPRESS)

    # Parse arguments
    args = parser.parse_args(args=args)

    # Configure logging
    _configure_logging(args.verbose)

    # Run the program
    try:
        success = _run(args, os.getcwd(), parser.error)
    except KeyboardInterrupt:
        logging.debug("command cancelled")
    else:
        if success:
            logging.debug("command succedded")
        else:
            logging.debug("command failed")
            sys.exit(1)


def _configure_logging(verbosity=0):
    """Configure logging using the provided verbosity level (0+)."""

    # Configure the logging level and format
    if verbosity == 0:
        level = DEFAULT_LOGGING_LEVEL
        default_format = DEFAULT_LOGGING_FORMAT
        verbose_format = VERBOSE_LOGGING_FORMAT
    elif verbosity == 1:
        level = VERBOSE_LOGGING_LEVEL
        default_format = verbose_format = VERBOSE_LOGGING_FORMAT
    elif verbosity == 2:
        level = VERBOSE2_LOGGING_LEVEL
        default_format = verbose_format = VERBOSE_LOGGING_FORMAT
    else:
        level = VERBOSE2_LOGGING_LEVEL
        default_format = verbose_format = VERBOSE2_LOGGING_FORMAT

    # Set a custom formatter
    logging.basicConfig(level=level)
    formatter = WarningFormatter(default_format, verbose_format)
    logging.root.handlers[0].setFormatter(formatter)


def _run(args, cwd, err):  # pylint: disable=W0613
    """Process arguments and run the main program.
    @param args: Namespace of CLI arguments
    @param cwd: current working directory
    @param err: function to call for CLI errors
    """
    return False


if __name__ == '__main__':  # pragma: no cover, manual test
    main()
