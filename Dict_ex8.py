import argparse
import sys
import os
import random as rd

parser = argparse.ArgumentParser() # create argument parser object
parser.add_argument("path_file", help = "path to the file .txt contain vector for reading")
#parser.add_argument ("--verbosity", help = "increase output verbosity")
args = parser.parse_args()
if not os.path.exists(args.path_file):
    print("No path {} exist".format(args.path_file))
    sys.exit(1)
else:
    f = open(args.path_file,"r")
    l =[]
    dicts ={
        "name": "",
        "value": [0]*2,
        "color": "black"
    }
    # A 3 4 red
    for line in f:
        txt = line.split()
        try:
            dicts["name"]     = txt[0]
            dicts["value"][0] = int(txt[1])
            dicts["value"][1] = int(txt[2])
            dicts["color"]    = txt[3]
            l.append(dicts.copy())
            print(dicts)
        except:
            print("data may wrong")
            sys.exit(1)
    #print(l)
    f.close()

    # create random value, color so we can create  D, E point and save in result file
    color_list =["Green", "Red", "Blue"]
    #print("a ==", int(a))
    result_file="result.txt"
    print("saving data to file ", result_file)
    try:
        f = open(result_file,"w")
        for i in range(2):
            for j in range(2):
                dicts["value"][j] = rd.randint(1,100) # random value
            dicts["name"] = chr(ord('D') + i)
            dicts["color"] = color_list[rd.randint(0,2)] # random color

            stri= dicts["name"] + " "+ str(dicts["value"][0]) + " " + str(dicts["value"][1]) + " " + dicts["color"] +"\n"
            
            print(stri,end="")
            f.write(stri)
        f.close()
    except:
        print("can save data")
