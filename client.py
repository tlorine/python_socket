#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

HOST = "192.168.31.17"
PORT = 10003

sock = socket.socket()
sock.connect((HOST, PORT))
while True:
    sock.send(input("введите число: ").encode())
    data = sock.recv(1024).decode()
    if not data:
        break
    print(data)    
sock.close()
