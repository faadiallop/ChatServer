#Created: 09/14/2023
#Creator: Faa Diallo
#Simple client to connect the TCP server and send a message to it.
import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    msg = bytes(input("What message would you like to send the server?\n"), "utf-8")
    s.sendall(msg)
    data = s.recv(1024)

print(f"Received \"{data.decode('utf-8')}\"")

