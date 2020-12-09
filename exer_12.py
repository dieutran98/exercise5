from point_class import point
import sys
import json
import os
import numpy as np
import math

dict_list = []
cmd_split = []
dict_data ={
    "name": "",
    "value": [0]*2,
    "color": ""
}

dict_operator ={
    "+": "addP",
    "-": "sub",
    "*": "mul",
    "/": "dev",
    "=": "result"
}
key = 1 # print result if key = 1 else dont
res = point(dict_data)
name = ""
error = 0
class switch_case:
    def __init__(self,cmd):
        method = getattr(self,cmd,lambda: "invalid")
        return method()

    def add(none):
        try: 
            dict_data["name"] = cmd_split[1]
            dict_data["value"] = [int( cmd_split[2]),int( cmd_split[3])]
            dict_data["color"] = cmd_split[4]
            dict_list.append( point(dict_data))
            print (dict_list)
            
        except:
            print("syntax error! please type: add name value color")
            global error
            error = 1
            

    def save(none):
        global error
        try:
            if not os.path.exists(cmd_split[1]):
                print("No path {} exist".format(cmd_split[1]))
                error = 1
            else:
                for obj in dict_list:
                    obj.save_json(cmd_split[1])
        except:
            print("syntax error! please type: save file_name.json")
            error = 1

    def dele(none):
        try:
            with open( cmd_split[1], "w") as save_f:
                save_f.write("")
            dict_list = []
            with open( "log.txt", "w") as save_f:
                save_f.write("")
        except:
            print("syntax error! please type: dele target_file")
            global error
            error = 1

    def import_data(none):
        global error
        try:
            if not os.path.exists(cmd_split[1]):
                print("No path {} exist".format(cmd_split[1]))
                error = 1
            else:
                with open( cmd_split[1], 'r') as openfile: 
                    json_object = json.load(openfile)
                #print(type(json_object))
                #print(dict_list)
                for obj in json_object:
                    dict_list.append(point(obj))
                #print(dict_list)
                print("Imported: ",end="")
                for obj in dict_list:
                    print("'{}',".format(obj.name),end=" ")
                print()
        except:
            print("syntax error! Please type: import_data file_name.json")
            error = 1
    
    def addP(none):
        try:
            for obj0 in dict_list:
                if obj0.name == cmd_split[0]:
                    #pa = obj0
                    break
            #print(obj0)
            for obj1 in dict_list:
                if obj1.name == cmd_split[2]:
                    #pb = obj1
                    break
            global res
            #print(obj1)
            res = obj0 + obj1
            res.name = name
            if key == 1:
                print (res.value)
            #return res.value
        except:
            print("syntax error! Please type: <point> + <point>")
            global error
            error = 1

    def sub(none):
        try:
            for obj0 in dict_list:
                if obj0.name == cmd_split[0]:
                    #pa = obj0
                    break
            #print(obj0)
            for obj1 in dict_list:
                if obj1.name == cmd_split[2]:
                    #pb = obj1
                    break
            global res
            #print(obj1)
            res = obj0 - obj1
            res.name = name
            if key == 1:
                print (res.value)
            #return res.value
        except:
            print("syntax error! Please type: <point> - <point>")
            global error
            error = 1
        
    def result(none):
        try:
            global cmd_split
            global key
            global name
            key = 0
            name = cmd_split[0]
            operator = cmd_split[3]
            cmd_split = cmd_split[2:]
            #print(cmd_split)
            switch_case(dict_operator[cmd_split[1]])
            #print(res.convert_dict())
            res.print()
            dict_list.append(point(res.convert_dict()))
            #print("add {} to dict_list".format(res.name))
            key = 1
            #return res
        except:
            print("syntax error! Please type: <point> = <point> <operator> <point>")
            global error
            error = 1
        
    def help(none):
        print("Usage: add <name> <value>(list) <color> ")
        print("       <point> <operator> <point> ")
        print("       <point> = <point> <operator> <point> ")
        print("       import_data file_name.json ")
        print("       dele target_file")
        print("       save file_name.json")
        print("       <point>.len")
    
    def len(none):
        # get point name
        #print(cmd_split[0][0])
        try:
            for obj1 in dict_list:
                if obj1.name == cmd_split[0][0]:
                    #pb = obj1
                    break
            a = obj1.value[0]
            b = obj1.value[1]
            res = math.sqrt(a*a + b*b)
            print(res)
        except:
            global error
            error = 1
#def import_data():

while True:

    command = input("enter your input: ")
    cmd_split = command.split()
    error = 0
    try:
        if cmd_split[0] == "exit":
            break
        try:
            switch_case( dict_operator[ cmd_split[1]])
        except:
            try:
                switch_case(cmd_split[0])
            except:
                try:
                    switch_case(cmd_split[0][2:])
                except:
                    print("syntax error!")
                    print("type 'help' for help")
                    continue
        # save comand in log
        if error == 0:
            with open("log.txt", "a") as log_file:
                command += "\n"
                log_file.write(command)
    except:
        print("syntax error!")
        print("type 'help' for help")

    