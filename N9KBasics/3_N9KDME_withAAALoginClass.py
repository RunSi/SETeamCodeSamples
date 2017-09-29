#! /usr/bin/env python3
__author__ = 'sihart'

import json

import requests

from classes.N9K_aaa_login import AAALogin


username = "vagrant"
password = "vagrant"
ip_addr =  "127.0.0.1:8443"


payload = {
  "topSystem": {
    "children": [
      {
        "interfaceEntity": {
          "children": [
            {
              "l1PhysIf": {
                "attributes": {
                  "accessVlan": "vlan-20",
                  "descr": "from_post",
                  "id": "eth1/2"
                }
              }
            },
            {
              "l1PhysIf": {
                "attributes": {
                  "accessVlan": "vlan-20",
                  "descr": "from_post",
                  "id": "eth1/3"
                }
              }
            }
          ]
        }
      }
    ]
  }
}



def post(auth_cookie, url, payload):
    response = requests.request("POST", url, data=json.dumps(payload),
                                cookies=auth_cookie, verify=False)

    print()
    print ("POST RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))


if __name__ == '__main__':
    n9klogin = AAALogin(username, password, ip_addr)
    status, auth_cookie = n9klogin.getcookie()
    print(status)
    if status == requests.codes.ok:
        url = "https://" + ip_addr + "/api/mo/sys.json"
        post(auth_cookie, url, payload)
        n9klogin.aaa_logout()