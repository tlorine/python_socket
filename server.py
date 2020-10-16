import socket
from threading import Thread

HOST = socket.gethostbyname(socket.gethostname())
PORT = 10003

print(HOST)

def mailing_proc(conn, user_name):
    while True:
        data = conn.recv(1024).decode() #принимает данные от клиента(размер данных)
        print(data)
        if data == "/exit":
            users_list[user_name].send(f"/exit".encode())
            break
        for key in users_list:
            if key != user_name:
                users_list[key].send(f"{user_name}:\t{data}".encode())

users_list = dict()
sock = socket.socket() # создания сокета
sock.bind((HOST, PORT)) #связать с хостом и портом 
sock.listen(2) #cокет теперь слушает подлючения (принимает 1 аргумент - сколько подклчений возможно за раз)
while True:
    conn, addr = sock.accept() #ждет клиента. возращает новый сокет и номер клиента
    user_name = conn.send("Enter Login:".encode())
    users_list[user_name] = conn
    mailing = Thread(target=mailing_proc, args=(conn, user_name))
    mailing.start()
sock.close()