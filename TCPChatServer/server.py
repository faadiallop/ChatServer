#Created 09/14/2023
#Creator: Faa Diallo
#This is a TCP server which functions as a chat room. 
#The client receives all of the messages that are sent to the server.
import socket

HOST = ""
PORT = 65432

def bytesToStr(bytes_data):
    """
    bytesToStr takes in a bytes variable and converts it to a string.
    :param bytes_data: data in bytes.
    :return string: the bytes variable as a string.
    """

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on port {PORT} for packets.")
        print("-----Server Up------")
        conn, addr = s.accept()
        with conn:
            #The first piece of data that's expected is the username.
            username = conn.recv(1024)
            print(f"User {bytesToStr(username)} has entered the chat room.")
        while True:
            data = conn.recv(1024)
            if not data: 
                print(f"User {bytesToStr(username)} has logged off.")
                break
            data = bytes(f"{bytesToStr(username)}: ", "utf-8") + data
            conn.sendall(data)
            print(bytesToStr(data))

if __name__ == "__main__":
    main()

