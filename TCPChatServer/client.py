#Created: 09/14/2023
#Creator: Faa Diallo
#Simple client to connect the TCP server and send messages to it.
import socket

HOST = "127.0.0.1"
PORT = 65432

def prompt(prompt_msg):
    """
    prompt asks the user the message that is input.
    :param prompt_msg: message that the user is prompted with.
    :return string: the users response to the prompt.
    """
    return bytes(input(prompt_msg), "utf-8")

def bytesToStr(bytes_data):
    """
    bytesToStr takes in a bytes variable and converts it to a string.
    :param bytes_data: data in bytes.
    :return string: the bytes variable as a string.
    """
    return bytes_data.decode('utf-8')

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        username = bytes(input("What is your username?\n"), "utf-8")
        s.sendall(username)
        while True:
            msg = prompt("")
            if not msg: break
            s.sendall(msg)
            data = s.recv(1024)
            print(bytesToStr(data))

if __name__ == "__main__":
    main()

