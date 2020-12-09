#!/usr/local/bin/python3.9

import sys
import argparse
import os

def Sum():
    #check python version
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro
    if not (major >=3 and minor>=9):
        print("This script requires Python 3.9 or higher!")
        print("You are using Python {}.{}.{}".format(major, minor, micro))
        sys.exit(1)
    else:
        parser = argparse.ArgumentParser() # create argument parser object
        parser.add_argument("path_file", help = "path to the file .txt used to read")
        #parser.add_argument ("--verbosity", help = "increase output verbosity")
        args = parser.parse_args()
        #if args.verbosity:
        if not os.path.exists(args.path_file):
            print("No path {} exist".format(args.path_file))
        else: 
            #print(args.path_file)
            f=open(args.path_file,"r")
            s = f.read()
            print("Reading file... ")
            print(s)
            print("Calcualting sum...")
            sum = 0
            l=""
            for n in s.split():
                if n.isdigit():
                    if not l:
                        l+=n
                    else:
                        l+=" + "
                        l+=n
                    sum = sum + int(n)
            print(l, end= " = ")
            print(sum)
Sum()
