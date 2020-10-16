import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 10003

print(HOST)

sock = socket.socket() # создания сокета
sock.bind((HOST, PORT)) #связать с хостом и портом 
sock.listen(1) #cокет теперь слушает подлючения (принимает 1 аргумент - сколько подклчений возможно за раз)
conn, addr = sock.accept() #ждет клиента. возращает новый сокет и номер клиента
while True:
    data = conn.recv(1024).decode() #принимает данные от клиента(размер данных)

    try:
        responce = "result: " + str(int(data) / 2)
    except:
        responce = "not a number"
    if data == "end":
        break
    print(f"cleint: {data}")
    conn.send(responce.encode())
sock.close()