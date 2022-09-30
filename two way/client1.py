import socket
HOST = "127.0.0.1"
PORT = 5555

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        send = input(">")
        s.sendall(bytes(send,"utf-8"))
        data = s.recv(1024)
        print("Received:",data.decode("utf-8"))


