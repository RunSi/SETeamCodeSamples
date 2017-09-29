#! /usr/bin/env python3
__author__ = 'sihart'

import json
import requests
import xmltodict


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
    "output_format": "xml"
  }
}

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword))

myxml = xmltodict.parse(response.text)

print(myxml)