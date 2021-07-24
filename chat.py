from tkinter import *
from tkinter import ttk
import threading, socket, time

msg=[]

def Server():
    myIP = '192.168.9.205'
    port = 5000

    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server.bind((myIP, port))
        server.listen(1)

        print('Waiting connection from clients...\n')

        client, addr = server.accept()
        print('Connect from: ', str(addr))

        data = client.recv(1024).decode('utf-8')

        msg.append(data)

        try:
            textShow = ''
            if len(msg) >= 5:
                for m in msg[-5]:
                    textShow += m + '\n'
            else:
                for m in msg:
                    textShow += m + '\n'
            v_result2.set(textShow)
        except:
            v_result2.set('')
        resp_text = 'Received'

        client.send(resp_text.encode('utf-8'))
        client.close()

def ThreadServer():
    task1 = threading.Thread(target=Server)
    task1.start()

def Client():
    server_ip = '192.168.9.205'
    port = 5000
    data = v_message.get()

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.connect((server_ip, port))
    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    server.close()

def Send(event=None):
    text = v_message.get()
    v_result1.set(text)
    task2 = threading.Thread(target=Client)
    task2.start()
    # time.sleep(5)
    # v_message.set('')
    # e_message.focus()

root = Tk()
root.geometry('500x300')
root.title('Python socket chat')

english = ('Times New Roman', 15)

f1 = Frame(root)
f1.pack(pady=5)

v_message = StringVar()
e_message = ttk.Entry(f1, textvariable=v_message, font=english)
e_message.grid(row=0, column=0)
e_message.focus()

b_send = ttk.Button(f1, text='Send', command=Send)
b_send.grid(row=0, column=1)

f2 = Frame(root)
f2.pack(pady=5)

v_result1 = StringVar()
v_result1.set('-=server msg=-')
e_result1 = Label(f2, textvariable=v_result1, font=english)
e_result1.grid(row=1, column=0)

v_result2 = StringVar()
v_result2.set('-=client msg=-')
e_result2 = Label(f2, textvariable=v_result2, font=english)
e_result2.grid(row=1, column=1)

root.bind('<Return>', Send)
root.bind('<Escape>', lambda x: root.destroy())

ThreadServer()

root.mainloop()
