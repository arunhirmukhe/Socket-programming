from telnetlib import DO


import socket

if __name__ == "__main__":
  ip = "127.0.0.1"
  port = 1234

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((ip, port))
  server.listen(5)
  client, address = server.accept()
  while True: 
    
    print("waiting....") 
    string = client.recv(1024)
    string = string.decode("utf-8")
    print(string)

    client.close()  

   
#  print(f"Connection Established = {address[0]}:{address[1]}")

