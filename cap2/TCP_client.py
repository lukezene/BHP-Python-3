#!/usr/bin/env python


import socket

target_host = "www.google.com" #"127.0.0.1"
target_port = 80 #9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
#client.send(b"ABCDEF")

# receive some data
response = client.recv(4096)

print(response.decode())
