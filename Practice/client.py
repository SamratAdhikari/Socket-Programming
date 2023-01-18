# client

import socket

HOST = socket.gethostname()
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
	msg = sock.recv(1024)
	print(msg.decode('utf-8'))
