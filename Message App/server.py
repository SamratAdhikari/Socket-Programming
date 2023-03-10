# Server

import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = "192.168.1.66"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
# print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")

	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)

		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
		
			if msg == DISCONNECT_MSG:
				connected = False

			print(f"[{addr}]: {msg}")

			ask = str(input("Enter the message to send: "))
			conn.send(ask.encode(FORMAT))

	conn.close()


def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")

	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()

		print(f"\n[ACTIVE CONNECTIONS] {threading.activeCount() - 1}\n")

print("[STARTING] Server is starting...")
start()

server.close()

