import os
import json
import sys

dict_list = []
while True:

    command = input("enter your in put: ")
    cmd_split = command.split()

    
    point_dict = {
        "name": "",
        "value": [0,0],
        "color": "black"
    }

    if cmd_split[0] == "add":
        try: 
            point_dict["name"]= cmd_split[1]
            point_dict["value"]= [int( cmd_split[2]), int( cmd_split[3])]
            point_dict["color"]= cmd_split[4]
            dict_list.append(point_dict.copy())
            print (dict_list)
        except:
            print("syntax error! please type: add name value color")
    if cmd_split[0] == "exit":
        break
    if cmd_split[0] == 'save':
        try:
            if not os.path.exists(cmd_split[1]):
                print("No path {} exist".format(cmd_split[1]))
                continue
            with open(cmd_split[1], "w") as save_f:
                save_f.write(json.dumps(dict_list, indent=4))
        except:
            print("syntax error! please type: save file_name")


