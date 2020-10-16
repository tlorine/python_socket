import socket
from threading import Thread

HOST = socket.gethostbyname(socket.gethostname())
PORT = 10000

users_list = dict()

print(HOST)

def mes(name, mes, all_usr=True):
    for key in users_list:
        if all_usr == False and key == name:
            continue
        users_list[key].send(f"{name}: {mes}".encode())

def mailing_proc(conn, users_list):
    user_name = conn.recv(1024).decode()
    users_list[user_name] = conn
    mes("server", f"{user_name} connected")
    while True:
        data = conn.recv(1024).decode() #принимает данные от клиента(размер данных)
        print(data)
        if data == "/exit":
            users_list[user_name].send(f"/exit".encode())
            conn.recv(1024).decode()
            mes("server", f"{user_name} disconnected")
            break
        mes(user_name, f"{data}", all_usr=False)

sock = socket.socket() # создания сокета
sock.bind((HOST, PORT)) #связать с хостом и портом 
sock.listen(5) #cокет теперь слушает подлючения (принимает 1 аргумент - сколько подклчений возможно за раз)
while True:
    conn, addr = sock.accept() #ждет клиента. возращает новый сокет и номер клиента
    conn.send("Enter Login:".encode())
    mailing = Thread(target=mailing_proc, args=(conn, users_list))
    mailing.start()
sock.close()