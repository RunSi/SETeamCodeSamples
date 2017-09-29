#! /usr/bin/env python3
__author__ = 'sihart'




import requests
import json

#We are not checking Certs because of verify False.  Therefore this code suppresses warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class AAALogin():
    '''a class for logging into NXoS, username, password and IP address required'''
    def __init__(self, username, password, ip_addr):
        self.username = username
        self.password = password
        self.ip_addr = ip_addr

    def __repr__(self):
        fmt = '{} for user {} at ip address {})'
        return fmt.format(type(self).__name__, self.username, self.ip_addr)



    def getcookie(self):
        '''Obtain a cookie for subsequent requests to NXoS'''
        payload = {
            'aaaUser': {
                'attributes': {
                    'name': self.username,
                    'pwd': self.password
                }
            }
        }
        url = "https://" + self.ip_addr + "/api/aaaLogin.json"
        self.auth_cookie = {}

        self.response = requests.request("POST", url, data=json.dumps(payload), verify=False)
        if self.response.status_code == requests.codes.ok:
            data = json.loads(self.response.text)['imdata'][0]
            token = str(data['aaaLogin']['attributes']['token'])
            self.auth_cookie = {"APIC-cookie": token}
        return(self.response.status_code, self.auth_cookie)

    def aaa_logout(self):
        payload = {
            'aaaUser': {
                'attributes': {
                    'name':self.username
                }
            }
        }
        url = "https://" + self.ip_addr + "/api/aaaLogout.json"

        response = requests.request("POST", url, data=json.dumps(payload),
                                    cookies=self.auth_cookie, verify=False)

        print()
        print("aaaLogout RESPONSE:")
        print(json.dumps(json.loads(response.text), indent=2))
        print(response.status_code)
        print()
