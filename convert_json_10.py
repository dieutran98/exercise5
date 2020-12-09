import os
import json
import sys
import argparse
import random as rd

parser = argparse.ArgumentParser() # create argument parser object
parser.add_argument("path_file", help = "path to the file .txt used to read")
#parser.add_argument ("--verbosity", help = "increase output verbosity")
args = parser.parse_args()
if not os.path.exists(args.path_file):
    print("No path {} exist".format(args.path_file))
    sys.exit(1)
else:

    class point:
        def __init__(self, name, value, color ):
            self.name = name 
            #self.value = [0]*2
            self.value = value # value is a list
            self. color = color
        """
        def __init__(self):
            self.name = ""
            self.value = [0]*2
            self. color = ""
        """

        def print(self):
            print ("name = {name} \nvalue = {value}\ncolor = {color} ".format(name=self.name, value=self.value, color=self.color))
            print("===================================================================")

        def save_json(self, save_file):
            point_dict={
                "name": self.name,
                "value": self.value,
                "color": self.color
            }
            content = []
            #check if file isn't empty then do code below
            if not os.stat(save_file).st_size == 0:
                with open(save_file,"r") as save_f:
                    content = ( json.load(save_f))
            # if file is empty just need to do code below
            content.append(point_dict)
            json_obj = json.dumps(content, sort_keys = True, indent=4)
            with open(save_file, "w") as save_f: 
                save_f.write(json_obj)


    f = open(args.path_file,"r")
    object_list = []
    try:
        for line in f:
            txt = line.split()
            object_list.append( point( txt[0], [ int( txt[1]), int( txt[2])], txt[3]))
            #                            ^              ^              ^         ^
            #                          name           val0            val1     color
    except:
        print("can't read data in file '{}'".format(args.path_file))
        sys.exit(1)
    f.close()
    for obj in object_list:
        obj.print()

    # create random value, color so we can create  D, E point and save in result file
    color_list =["Green", "Red", "Blue"]
    obj = point("", [0] * 2, "") # give some default value
    save_file = "save.json"
    for i in range(2):
        for j in range(2):
            obj.value[j] = rd.randint(1,100) # random value
        obj.name = chr(ord('D') + i)
        obj.color = color_list[rd.randint(0,2)] # random color
        obj.print()
        try: 
            obj.save_json(save_file)
        except:
            print("can't read data in file '{}'".format(save_file))

    """
    #read json_file
    with open('json_save.json', 'r') as openfile: 
        json_object = json.load(openfile)
    print(json_object)
    """