import argparse
import json
import os
import sys

import jinja2
import requests

from N9K_aaa_login import AAALogin

parser = argparse.ArgumentParser()
parser.add_argument('-v', action='append', dest="vlans", default=[], help='add repeated vlans to a list')

parser.add_argument('-i', '--ipaddr',  default="127.0.0.1:8443", help="Enter the IP or URL for the N9k/3k")
parser.add_argument('-u', '--user-val',  default="vagrant", help='enter username for Nexus9K or 3K')
parser.add_argument('-p', '--passw', default="vagrant", help="Enter password for Nexus9k/3k")


args = parser.parse_args()

print(args.user_val)
print(args.passw)
newvlans = []
newvlans = [r'"' + x + r'"' for x in args.vlans]


def post(auth_cookie, url, payload):
    response = requests.request("POST", url, data=payload,
                                cookies=auth_cookie, verify=False)

    print()
    print ("POST RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))


if __name__ == '__main__':
    n9klogin = AAALogin(args.user_val, args.passw, args.ipaddr)
    status, auth_cookie = n9klogin.getcookie()
    print(status)
    print(auth_cookie)

    #loader = jinja2.FileSystemLoader(os.getcwd())
    loader = jinja2.FileSystemLoader(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')))
    jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    template = jenv.get_template('N9KJinjaLooVlan.j2')

    confpayload = template.render(vlans=newvlans)
    print(confpayload)


    if status == requests.codes.ok:
        url = "https://" + args.ipaddr + "/api/mo/sys.json"
        post(auth_cookie, url, confpayload)
        n9klogin.aaa_logout()