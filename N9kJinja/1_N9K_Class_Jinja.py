#! /usr/bin/env python3
__author__ = 'sihart'


import json
import os

import jinja2
import requests

from N9K_aaa_login import AAALogin

"""
Modify these please
"""
username = "vagrant"
password = "vagrant"
ip_addr =  "127.0.0.1:8443"



def aaa_logout(username, ip_addr, auth_cookie):
    payload = {
        'aaaUser' : {
            'attributes' : {
                'name' : username
                }
            }
        }
    url = "https://" + ip_addr + "/api/aaaLogout.json"

    response = requests.request("POST", url, data=payload,
                                cookies=auth_cookie, verify=False)

    print()
    print ("aaaLogout RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))
    print()


def post(auth_cookie, url, payload):
    response = requests.request("POST", url, data=payload,
                                cookies=auth_cookie, verify=False)

    print()
    print ("POST RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))


if __name__ == '__main__':
    n9klogin = AAALogin(username, password, ip_addr)
    status, auth_cookie = n9klogin.getcookie()
    print(status)

    #loader = jinja2.FileSystemLoader(os.getcwd())
    loader = jinja2.FileSystemLoader(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')))
    jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    template = jenv.get_template('n9kJinja.j2')
    confpayload = template.render(if_name=r'"eth1/5"', description=r'"JinjaStuff5"')
    print(confpayload)



    if status == requests.codes.ok:
        url = "https://" + ip_addr + "/api/mo/sys.json"
        post(auth_cookie, url, confpayload)
        aaa_logout(username, ip_addr, auth_cookie)