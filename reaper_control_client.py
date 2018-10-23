# Client script to send data to the server to run commands to 
# control my DAW

import socket
import sys

HOST = '127.0.0.1'    # The remote host
PORT = 6666              # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        user_input = input("\nEnter your command:")
        s.sendall(user_input.strip().encode())
        data = s.recv(1024)
        command = data.strip().decode()
        if command == "endme":
            break

sys.exit(1)
