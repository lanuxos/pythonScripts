# EP.13 Python Socket
# Client
import socket

# serverip = '159.65.135.242'
# port = 9090
serverip = '192.168.9.205'
port = 9000

while True:
    data = input('Send message: ')
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.connect((serverip, port))
    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print('Data from server: ', data_server)
    server.close()