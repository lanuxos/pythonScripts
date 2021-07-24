# EP.3 Python sockett
# Server
import socket

serverip = '192.168.9.205'
port = 9000

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((serverip, port))
    server.listen(1)

    print('Waiting for connection ::..')

    client, addr = server.accept()

    print('Connected from: ', addr)

    data = client.recv(1024).decode('utf-8')

    print('Message from client [', addr, '] >>> ', data)

    text = 'Server received your request and data.'
    client.send(text.encode('utf-8'))
    client.close()