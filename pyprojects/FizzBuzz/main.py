#!/usr/bin/env python3

"""Simple fizzbuzz generator.

This script prints out a sequence of numbers from a provided range
with the following restrictions:

- if the number is divisible by 3, then print out "fizz",
- if the number is divisible by 5, then print out "buzz",
- if the number is divisible by 3 and 5, then print out "fizzbuzz".
"""

import logging
import logging.handlers
import os
import argparse
import sys

logger = logging.getLogger(os.path.splittext(os.path.basename(sys.argv[0]))[0])


class CustomFormatter(argparse.RawDescriptionHelpFormatter,
                      argparse.ArgumentDefaultsHelpFormatter):
    pass


def parse_args(args=sys.argv[1:]):
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
        formatter_class=CustomFromatter)

    g = parser.add_argument_group("fizzbuzz settings")
    g.add_argument("--fizz", metavar="N",
                   default=3,
                   type=int,
                   help="Modulo value for fizz")
    g.add_argument("--buzz", metavar="N",
                   default=5,
                   type=int,
                   help="Modulo value for buzz")

    debugSilent = parser.add_mutually_exclusive_group()
    debugSilent.add_argument("--debug", "d", action="store_true",
                             default=False,
                             help="enable debugging")
    debugSilent.add_argument("--silent", "s", action="store_true",
                             default=False,
                             help="don't log to console")
    
    parser.add_argument("start", type=int, help="Start value")
    parser.add_argument("end", type=int, help="End value")

    return parser.parse_args(args)


def setup_logging(options):
    """Configure logging."""
    root = logging.getLogger("")
    root.setLevel(logging.WARNING)
    logger.setLevel(options.debug and logging.DEBUG or logging.INFO)
    if not options.silent:
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter(
            "%(levelname)s[%(name)s] %(message)s"
        ))
        root.addHandler(ch)


if __name__ == "__main__":
    options = parse_args()
    setup_logging(options)

    try:
        logger.debug("compute fizzbuzz from {} to {}".format(options.start,
                                                             options.end))
        for n in range(options.start, options.end + 1):
            if n % 3 == 0 and n % 5 == 0:
                print("fizzbuzz")
            elif n % 3 == 0:
                print("fizz")
            elif n % 5 == 0:
                print("buzz")
            else:
                print(n)
    except Exception as e:
        logger.exception("%s", e)
        sys.exit(1)
    sys.exit(0)
    