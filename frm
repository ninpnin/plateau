#! /usr/bin/python

import sys
import os
import argparse
from pyplateau.utils import get_available_dirs, get_current_dirs, get_files

def not_in_folder():
    print("Not in folder")

def main(args):
    if args.help:
        print("This is a help message for 'fls'.")
    else:
        selected_dirs = get_current_dirs()
        available_dirs = get_available_dirs()
        available_files = get_files(selected_dirs, available_dirs)

        if len(selected_dirs) == 0:
            print("Filesystem root")
        else:
            print("Current tags:")
            print(" ".join(selected_dirs))
            files = get_files(selected_dirs, available_dirs)
            if len(files) == 0:
                not_in_folder()
            else:
                humanreadable_files = [f.split("_")[-1] for f in files]
                for rmfile in args.rmfiles:
                    if rmfile in humanreadable_files:
                        ix = humanreadable_files.index(rmfile)
                        filename = files[ix]
                        os.system("rm .files/" + filename)
                        for tag in selected_dirs:
                            dir_files = open(".dirs/" + tag).read().split()
                            dir_files = [f for f in dir_files if "_" + rmfile not in f]
                            d = open(".dirs/" + tag, "w")
                            d.write(" ".join(dir_files))
                            d.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", action='store_true')
    parser.add_argument("-a", "--all", action='store_true')
    parser.add_argument("rmfiles", type=str, nargs="*", default=[])
    args = parser.parse_args()
    main(args)

