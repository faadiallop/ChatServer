#Created 09/14/2023
#Creator: Faa Diallo
#This is a TCP server which functions as a chat room. The client receives
#all of the messages that are sent to the server.
import socket

HOST = ""
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print(f"Listening on port {PORT} for packets.")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            conn.sendall(data)
            print(data.decode('utf-8'))
print("The message has been echoed")
