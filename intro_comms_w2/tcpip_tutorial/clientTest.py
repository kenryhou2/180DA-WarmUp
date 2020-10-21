import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.239', 8081))
client.send("I am Client\n".encode())
from_server = client.recv(4096)
client.close()
print(from_server.decode('utf-8'))
