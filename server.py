#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:29:13 2020

@author: skbuddy
"""


import socket
#importing the module/library needed for socket programming

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#method socket is used to create an object s

local_hostname = socket.gethostname()
#gethostname is a method to get the name of the host i.e the system
#or you can provide it explicitly like 'skbuddy'

local_fqdn = socket.getfqdn()


ip_address = socket.gethostbyname(local_hostname)

print("working on %s (%s) with %s " % (local_hostname, local_fqdn, ip_address))

server_address = (ip_address, 5000)
print("starting up on %s port %s" % server_address)
s.bind((server_address))

s.listen(1)

while True:
    
    print("waiting for a connection")
    clt,adr = s.accept()
    
    try:
        print("Connections from ", adr)
        
        while True:
            data = clt.recv(10)
            data = data.decode("utf-8")
            data = int(data)
            if data:
                data = data*1.8 + 32
                data = str(data).encode("utf-8")
                clt.sendall(data)
            else:
                print("no more data.")
                break
           
    finally:
        s.close
        break                



        

