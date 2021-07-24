# python socket
# client

import socket

server_ip = '192.168.9.205'
port = 5000

while True:
    data = input('\nSend message: ')

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.connect((server_ip, port))

    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print('Response from server: ', data_server)
    server.close()