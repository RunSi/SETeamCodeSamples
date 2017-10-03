#! /usr/bin/env python3
__author__ = 'sihart'

import paramiko
import time

ip = '198.18.134.140'
username = 'admin'
password = 'C1sco12345'
port =22

remote_conn_pre = paramiko.SSHClient()

#use this to avoid error on windows machines
#remote_conn_pre.set_missing_host_key_policy(paramiko.WarningPolicy())

remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy)

remote_conn_pre.connect(ip, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)

def disable_paging(remote_conn):

    remote_conn.send('terminal length 0\n')
    time.sleep(1)

    output = remote_conn.recv(1000)

    return output


remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print(output)

disable_paging(remote_conn)

remote_conn.send("show int brief\n")
time.sleep(2)

output = remote_conn.recv(10000)

print(output.decode('ascii'))

remote_conn.send("show ip int brief\n")
time.sleep(2)

output = remote_conn.recv(10000)
print(output.decode('ascii'))

