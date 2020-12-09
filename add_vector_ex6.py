#!/usr/local/bin/python3.9

import sys
import numpy as np
import os
import argparse

# check version numpy
s = np.version.version
x=y=0
y = s.index('.')
major = int(s[x:y])
x=y+1
y = s.index('.',x)
minor = int(s[x:y])

"""
# get micro
micro = int(s[y+1:])
print(micro)
"""
# check numpy version
if not (major>=1 and minor>=18):
    print("This script requires numpy 1.18 or higher!")
    print("You are using numpy {}".format(np.version.version))
    sys.exit(1)
else:
    parser = argparse.ArgumentParser() # create argument parser object
    parser.add_argument("path_file", help = "path to the file .txt used to read")
    #parser.add_argument ("--verbosity", help = "increase output verbosity")
    args = parser.parse_args()
    if not os.path.exists(args.path_file):
            print("No path {} exist".format(args.path_file))
            sys.exit(2)
    else: 
        # open and read file
        f = open(args.path_file,"r")
        l_val = []
        error = 0
        print("reading file...")
        for line in f:
            l = []
            print(line,end="")
            for value in line.split():
                try:
                    l.append(int(value))
                except:
                    print("                  error, the input must be int\n")
                    error = 1
            l_val.append(l)
        f.close()

        print("\nadding vectors")
        vector = []
        for vec in l_val:
            vector.append(np.array(vec))
        vector_sum = np.array([0]*2)
        #print(vector_sum)
        #print(vector)
        l =""

        for x in vector:
            l += str(x)
            l += " + "
            vector_sum += x
        le = len(l)
        #print(le)
        l = l[0:le-3]
        print(l," = ",vector_sum)
        if error == 1:
            print("the result maybe wrong.\nDo you still want to save the result ?")
            choice = input("y/n?")
            if not choice == "y":
                sys.exit(0)
        # write result into result file
        try: 
            resutl_path = "result.txt"
            f = open(resutl_path,"w")
            s = str(vector_sum)
            le = len(s)
            s = s[1:le-1] # delete []
            s += "\n"
            #print("s=" ,s)
            #print("s type: " ,type(s))
            f.write(s)
            f.close()
        except:
            print("can't save data")

