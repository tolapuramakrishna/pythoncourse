import socket
HOST = '127.0.0.1'
PORT = 5000

#socket.AF_INET-ipv4 and socket.SOCK_STREAM- tcp
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST,PORT))
    message = input("Enter your query?: ")

    while message !='q':
        client_socket.send(message.encode())
        data=client_socket.recv(1024).decode()
        print("recieved data from server ", data)
        message = input("Enter your query?: ")
        
    client_socket.close()
if __name__=='__main__':
    main()