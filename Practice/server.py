# server

import socket

HOST = socket.gethostname()
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)


def connection():
	print("[RUNNING] Server is running...")
	connect = True
	while connect:
		try:
			conn, addr = sock.accept()
			print(f"[CONNECTED]\nConnection from {addr} has been established !")
			conn.send(bytes('Welcome to the server', 'utf-8'))

		except socket.error() as e:
			print(e)

connection()


def send():
	sent = True
	while sent:
		ask = str(input("Enter your message: "))
		
