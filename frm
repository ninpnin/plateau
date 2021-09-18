#! /usr/bin/python

import sys
import os
import argparse
from pyplateau.utils import (
    get_available_dirs,
    get_current_dirs,
    get_files,
)


def main(args):
    if args.help:
        print("This is a help message for 'fls'.")
    else:
        assert len(args.rmfiles) > 0, "Provide at least 1 file"
        filenames = args.rmfiles
        deletion_succesful = rm_files(filenames)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", action='store_true')
    parser.add_argument("-a", "--all", action='store_true')
    parser.add_argument("rmfiles", type=str, nargs="*", default=[])
    args = parser.parse_args()
    main(args)

