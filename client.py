#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from threading import Thread

def chat_wind():
    while chat_run == True:
        data = sock.recv(1024).decode()
        if data == "/exit":
            break
        print(data)

HOST = "192.168.31.93"
PORT = 10003
chat_run = True

sock = socket.socket()
sock.connect((HOST, PORT))
print(sock.recv(1024).decode())
sock.send(input().encode())
chat = Thread(target=chat_wind, args=())
chat.start()
while True:
    mess = input("MES: ")
    sock.send(mess.encode())
    if mess == "/exit":
        break
chat.join()
sock.close()
