#! /usr/bin/env python3
__author__ = 'sihart'

'''simple json parsing of txt file
   try to print out other values or conditions'''

import json

file = open("n9kjson.txt", "r")

jsonstring = file.read()

jsondict = json.loads(jsonstring)

for y in jsondict["ROW_interface"]:
    if y["state"]=="up":
        print(y["interface"], " is in an up state, and on vlan ", y["vlan"])

