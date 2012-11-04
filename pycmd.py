#!/usr/bin/python

import os
import sys


if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.exit("less argument: cmd str")

    LINE = sys.stdin.readline()

    while LINE:
        LINE = LINE.strip()
        exec(sys.argv[1])
        LINE = sys.stdin.readline()

