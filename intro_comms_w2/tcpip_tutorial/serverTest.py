import socket
serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#assigns a port for the server that listens to clients connecting to this port
serv.bind(('192.168.1.239', 8081))
serv.listen(5)
while True:
	conn, addr = serv.accept()
	from_client = ''
	while True:
		data = conn.recv(4096)
		if not data: 
			break

		from_client += data.decode('utf-8')
		print(from_client)
		conn.send("I am Server - Kenry\n")
	conn.close()
	print("client disconnected\n")