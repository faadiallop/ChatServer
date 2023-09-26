#Created 09/14/2023
#Creator: Faa Diallo
#This is a TCP server which functions as a chat room. 
#The client receives all of the messages that are sent to the server.
import socket
import select

HOST = ""
PORT = 65431

def bytesToStr(bytes_data):
    """
    bytesToStr takes in a bytes variable and converts it to a string.
    :param bytes_data: data in bytes.
    :return string: the bytes variable as a string.
    """
    return bytes_data.decode("utf-8")

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #The following line allows you to reuse the socket in case 
    #the socket exits prematurely. It simply sets this option
    #specific to the socket type you're using.
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen()
    print(f"Listening on port {PORT} for packets.")
    print("-----Server Up------")

    read_list = [server_sock]
    write_list = []
    count = 0
    while True:
        #This line uses the lists to get the sockets that are 
        #currently readable and writeable. This line is blocking.
        readable, writable, errored = select.select(read_list, write_list, [])
        for sock in writable:
            for msg in messages:
                sock.sendall(msg)
        messages = []
        for sock in readable:
            if sock is server_sock:
                client_sock, addr = server_sock.accept()
                read_list.append(client_sock)
                #You need to append to the write_list here so that whenever The
                #line that gets the readable and writable sockets from the lists
                #executes you get all of the writable sockets.
                write_list.append(client_sock)
                print(f"Received conection from {addr}")
            else:
                data = sock.recv(1024)
                messages.append(data)
                if not data:
                    sock.close()
                    read_list.remove(sock)
                    write_list.remove(sock)

        #This line is needed in order to refresh the writable list as you 
        #might have added new writable sockets in the previous loop.
        #readable, writable, errored = select.select(read_list, write_list, [])
        #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #    read_list.append(s)
        #    readable, writable, errored = select.select(read_list, write_list, [])
        #    while True:
        #        conn, addr = s.accept()
        #        with conn:
        #            print(addr)
        #            data = conn.recv(1024)
        #            if not data: 
        #                break
        #            data = print(bytesToStr(data))
            #The first piece of data that's expected is the username.
            #username = conn.recv(1024)
            #print(f"User {bytesToStr(username)} has entered the chat room.")
            #conn2, addr2 = s.accept()
                #with conn2:
                #    username2 = conn.recv(1024)
                #    print(f"User {bytesToStr(username)} has entered the chat room.")
                #while True:
                #    data = conn.recv(1024)
                #    if not data: 
                #        print(f"User {bytesToStr(username)} has logged off.")
                #        break
                #    data = bytes(f"{bytesToStr(username)}: ", "utf-8") + data
                #    conn.sendall(data)
                #    print(bytesToStr(data))

if __name__ == "__main__":
    main()

