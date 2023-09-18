#Created 09/14/2023
#Creator: Faa Diallo
#This is a TCP server that receives a message and echos it back to
#ths client. After that it closes the connection.
import socket

HOST = ""
PORT = 65432

def bytesToStr(bytes_data):
    return bytes_data.decode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print(f"Login to the server on {PORT}.")
    s.listen()
    conn1, addr1 = s.accept()
    print(f"Connected by {addr1}")
    with conn1:
        s.listen()
        conn2, addr2 = s.accept()
        print(f"Connected by {addr2}")
        while True:
            data1 = conn1.recv(1_000_000)
            print(bytesToStr(data1))

