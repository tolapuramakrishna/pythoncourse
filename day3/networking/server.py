import socket
HOST = 'localhost'
PORT = 5000

#socket.AF_INET-ipv4 and socket.SOCK_STREAM- tcp
def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((HOST,PORT))
    print('Server socket started')

    my_socket.listen()
    (conn,addess) = my_socket.accept()
    print('connected to',addess)
    while(True):
        data = conn.recv(1024).decode()
        # use data further 
        if not data:
            break
        print('From connected user', str(data))
        response = input("send response: ")
        conn.send(response.encode())
    # except Exception as ex:
    #     print(ex)

if __name__ == '__main__':
    main()
