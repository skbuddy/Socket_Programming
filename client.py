#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:36:42 2020

@author: skbuddy
"""


import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

local_hostname = socket.gethostname()

local_fqdn = socket.getfqdn()

ip_address = socket.gethostbyname(local_hostname)

server_address = (ip_address, 5000)
s.connect(server_address)
print("connecting to %s (%s) %s " % (local_hostname, local_fqdn, ip_address))

temperature_data = [15, 22, 21, 26, 25, 19]
for entry in temperature_data:
    print("Temperature in 'C : %s" % entry)
    
    entry = str(entry).encode("utf-8")
    s.sendall(entry)
    
    new_data = s.recv(64)
    new_data = new_data.decode("utf-8")
    new_data = float(new_data)
    print("The temperature in 'F :", round(new_data, 2))
    
    time.sleep(2)
    

s.close()


