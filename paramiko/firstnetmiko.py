#! /usr/bin/env python3
__author__ = 'sihart'

from netmiko import ConnectHandler

net_connect = ConnectHandler(device_type='cisco_nxos', ip='127.0.0.1', port='2222', username='vagrant', password='vagrant')

output = net_connect.send_command("show int brief")

print(output)