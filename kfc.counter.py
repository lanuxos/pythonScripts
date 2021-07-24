# KFC counter
from tkinter import *
from tkinter import ttk
import socket

try:
    serverip = '192.168.9.205'
    port = 9000

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
except:
    print('Server error')

def SendData(data):
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Data from server: ', data_server)

allmenu = {'C101': {'code': 'C101', 'title': 'Flied Chicken', 'price': 55},
           'C102': {'code': 'C102', 'title': 'Grilled Chicken', 'price': 65},
           'C103': {'code': 'C103', 'title': 'Chicken Wing', 'price': 75},
           'C104': {'code': 'C104', 'title': 'French Fried', 'price': 45},
           'C105': {'code': 'C105', 'title': 'Soda', 'price': 55},
           'C106': {'code': 'C106', 'title': 'Coke', 'price': 65},
}

GUI = Tk()
GUI.geometry('1024x760')
# GUI.state('zoomed')

FT = Frame(GUI)
Tab = ttk.Notebook(FT, width=505, height=500)

T1 = Frame(Tab)
T2 = Frame(Tab)

Tab.pack(expand=1)
FT.place(x=20, y=20)

Tab.add(T1, text='Hot Menu')
Tab.add(T2, text='All Menu')

# B1 = ttk.Button(T1, text='Flied Chicken')
# B1.grid(row=0, column=0, ipady=5, ipadx=5)
# B2 = ttk.Button(T1, text='Grilled Chicken')
# B2.grid(row=0, column=1, ipady=5, ipadx=5)
# B3 = ttk.Button(T1, text='Chicken Wing')
# B3.grid(row=0, column=2, ipady=5, ipadx=5)

current_table = {}

def UpdateTable():
    table.delete(*table.get_children())
    for mn in current_table.values():
        table.insert('', 'end', value=mn)

def AddItem(CODE):
    print(allmenu[CODE])
    item = allmenu[CODE]
    if CODE not in current_table:
        data = [item['code'], item['title'], item['price'], 1, item['price']]
        current_table[CODE] = data
    # table.insert('', 'end', value=data)
    else:
        data = current_table[CODE]
        cal = data[2] * (data[3] + 1)
        data[3] = data[3] + 1
        data[4] = cal
        current_table[CODE] = data
    # print(current_table)
    UpdateTable()

rownumber = 0
columnnumber = 0
for i, mn in enumerate(allmenu.values(), start=1):
    B = ttk.Button(T1, text=mn['title'], width=15, command= lambda x=mn['code']: AddItem(x))
    B.grid(row=rownumber, column=columnnumber, ipady=25)
    columnnumber += 1
    if i % 3 == 0:
        rownumber += 1
        columnnumber = 0

header = ['CODE', 'TITLE', 'PRICE', 'QUAN', 'TOTAL']
table = ttk.Treeview(GUI, columns=header, show='headings', height=30)
table.place(x=600, y=20)

for hd in header:
    table.heading(hd, text=hd)

hwidth = [50, 120, 90, 50, 100]
for w, hd in zip(hwidth, header):
    table.column(hd, width=w)

ordernumber = 0

v_ordernumber = StringVar()
v_ordernumber.set('#{}'.format(ordernumber))
Lordernumber = ttk.Label(GUI, textvariable=v_ordernumber, font=('Times New Roman', 15), foreground='purple')
Lordernumber.place(x=100, y=650)

def ClearTable():
    global current_table
    table.delete(*table.get_children())
    current_table = {}

def Order():
    global ordernumber
    # convert dict to string
    text = '#ONB: {}'.format(ordernumber)
    for mn in current_table.values():
        txt = 'C:{}, Q:{}|'.format(mn[0], mn[3])
        text += txt
    print(text)
    SendData(text)
    ClearTable()
    ordernumber += 1
    v_ordernumber.set('#{}'.format(ordernumber))

BFRAME = Frame(GUI)
BFRAME.place(x=500, y=650)
BOrder = ttk.Button(BFRAME, text='Order', command=Order)
BOrder.pack(ipadx=5, ipady=10)

GUI.mainloop()
