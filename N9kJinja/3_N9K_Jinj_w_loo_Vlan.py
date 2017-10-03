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

# username = "admin"
# password = "cisco123"
# ip_addr =  "10.10.20.58"




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

    loader = jinja2.FileSystemLoader(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','templates')))
    jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    template = jenv.get_template('n9KJinjaLooVlan.j2')

    vlans = [r'"vlan-800"',r'"vlan-900"']

    confpayload = template.render(vlans=vlans)
    print(confpayload)


    if status == requests.codes.ok:
        url = "https://" + ip_addr + "/api/mo/sys.json"
        post(auth_cookie, url, confpayload)
        #aaa_logout(username, ip_addr, auth_cookie)
        n9klogin.aaa_logout()