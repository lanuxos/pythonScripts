# pyhoon socket
# server
import socket
from uncleengineer import thaistock

myip = '192.168.9.205'
port = 5000

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((myip, port))
    server.listen(1)

    print('Waiting connection from clients...\n')

    client, addr = server.accept()
    print('Connect from: ', str(addr))

    data = client.recv(1024).decode('utf-8')
    print('Msg from client: ', data)
    '''
    if data == 'lanuxos':
        resp_text = 'Msg received, lanuxos'
    elif data == 'vath':
        resp_text = 'Msg received, vath'
    else:
        resp_text = 'Msg received, Anonymous'
    '''
    try:
        stock = thaistock(data)
        resp_text = 'ITD stock: {}'.format(stock[1])
    except:
        resp_text = 'Fetching failed'
    client.send(resp_text.encode('utf-8'))
    client.close()