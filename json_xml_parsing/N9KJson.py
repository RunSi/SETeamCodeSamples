#! /usr/bin/env python3
__author__ = 'sihart'

import json
import requests


url='http://127.0.0.1:8000/ins'
switchuser='vagrant'
switchpassword='vagrant'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show int brief",
    "output_format": "json"
  }
}

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

file = open("n9kjson2.txt", "w")
file.write(json.dumps(response["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]))
file.close()

print(json.dumps(response["ins_api"]["outputs"], indent=4))