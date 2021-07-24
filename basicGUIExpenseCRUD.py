# EP.9
# GUIBasicExpense.py
from tkinter import *
from tkinter import ttk, messagebox
import csv, datetime
import sqlite3

conn = sqlite3.connect('expense.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS expenselist (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    transactionid TEXT,
    datetime TEXT,
    title TEXT,
    expence REAL,
    quantity INTEGER,
    total REAL
    )""")

def insert_expense(transactionid, datetime, title, expense, quantity, total):
    ID = None
    with conn:
        c.execute("""INSERT INTO expenselist VALUES(?,?,?,?,?,?,?)""", 
            (ID, transactionid, datetime, title, expense, quantity, total))
        conn.commit()

def show_expense():
    with conn:
        c.execute("SELECT * FROM expenselist")
        expense = c.fetchall()
        # print(expense)
        return expense

def update_expense(transactionid, title, expence, quantity, total):
    with conn:
        c.execute("""UPDATE expenselist SET 
            title = (?), 
            expence = (?), 
            quantity = (?), 
            total = (?) 
            WHERE transactionid = (?)""",  
            ([title, expence, quantity, total, transactionid]))
    conn.commit()
    # print('Database updated')

def delete_expense(transactionid):
    with conn:
        c.execute("""DELETE FROM expenselist WHERE transactionid=?""", ([transactionid]))
    conn.commit()
    # print('Record deleted')

GUI = Tk()
GUI.title('-= Expense Recorder by L@ =-')
# width=500, height=300, left-margin=400, top-margin=50
# GUI.geometry('500x400+400+50')
w = 500
h = 400

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')

menubar = Menu(GUI)
GUI.config(menu=menubar)


def About():
    messagebox.showinfo('About', 'This app saves expense list for you')


filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Import Excel')
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=About)
donatemenu = Menu(menubar)
menubar.add_cascade(label='Donate', menu=donatemenu)

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)  # width = 300, height = 500
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)  # expand to the max of GUI frame(500x400)

icon_1 = PhotoImage(file='asset/expense.png')
Tab.add(T1, text=f'{"Expense":^{15}}', image=icon_1, compound='top')  # top/botton/left/right
icon_2 = PhotoImage(file='asset/income.png')
Tab.add(T2, text=f'{"Summary":^{15}}', image=icon_2, compound='top')

F1 = Frame(T1)
# F1.place(x=105, y=10)
F1.pack()
days = {'Mon': 'ວັນຈັນ', 'Tue': 'ອັງຄານ', 'Wed': 'ພຸດ', 'Thu': 'ພະຫັນ', 'Fri': 'ສຸກ', 'Sat': 'ເສົາ', 'Sun': 'ອາທິດ'}


def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    amount = v_amount.get()

    if expense == '':
        # print('No expense item')
        messagebox.showinfo('Notice', 'Please fill expense field')
        return
    elif price == '':
        # print('No price')
        messagebox.showinfo('Notice', 'Please fill price field')
        return
    elif amount == '':
        amount = 1

    try:
        total = float(price) * float(amount)
        result.set(f'{expense.capitalize()} costs {float(price)} / piece, {amount} pieces cost {total}')

        now = datetime.datetime.now()
        d = now.strftime("%a")
        log = days[d] + '-' + now.strftime("%x")
        # log = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")

        transaction = now.strftime('%y%m%d%H%M%f')  # generate transaction id for update or delete

        # print(log, expense, price, amount, total)

        v_expense.set('')
        v_price.set('')
        v_amount.set('')

        insert_expense(transaction, log, expense, float(price), int(amount), total)

        # a - append, w - write (which remove existed record)
        with open('expense.csv', 'a', encoding='utf-8', newline='') as f:
            fw = csv.writer(f)
            data = [transaction, log, expense, price, amount, total]
            fw.writerow(data)
        UpdateTable()
        E1.focus()
    except:
        print('Error')
        # messagebox.showerror('Error', 'Please enter the valid input')
        messagebox.showwarning('Error', 'Please enter the valid input')
        # messagebox.showinfo('Error', 'Please enter the valid input')
        v_expense.set('')
        v_price.set('')
        v_amount.set('')

        E1.focus()


GUI.bind('<Return>', Save)
GUI.bind('<Escape>', lambda x: GUI.destroy())

FONT1 = ('Times New Roman', 12)
FONT2 = ('Defago Noto Sans', 8)

icon_4 = PhotoImage(file='asset/wallet.png')
L = ttk.Label(F1, image=icon_4)
L.pack()

L = ttk.Label(F1, text='Expense item', font=FONT1).pack()
v_expense = StringVar()
E1 = ttk.Entry(F1, textvariable=v_expense, font=FONT1)
E1.pack()

L = ttk.Label(F1, text='Price', font=FONT1).pack()
v_price = StringVar()
E2 = ttk.Entry(F1, textvariable=v_price, font=FONT1)
E2.pack()

L = ttk.Label(F1, text='Amount', font=FONT1).pack()
v_amount = StringVar()
E3 = ttk.Entry(F1, textvariable=v_amount, font=FONT1)
E3.pack()

icon_3 = PhotoImage(file='asset/save.png')
B2 = ttk.Button(F1, text='- Save -', command=Save, image=icon_3, compound='left')
B2.pack(ipadx=15, ipady=10, pady=5)

result = StringVar()
result.set("-= Result display here =-")
L = ttk.Label(F1, textvariable=result, font=FONT1, foreground='green')
L.pack()


def ReadCSV():
    with open('expense.csv', newline='', encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
        return data
        # print(data)


style = ttk.Style()
style.configure("Treeview.Heading", font=FONT2)
style.configure("Treeview", font=FONT2)

L = ttk.Label(T2, text='Summary Table', font="FONT1").pack(pady=5)

header = ['ລະຫັດ', 'ວັນເວລາ', 'ລາຍການ', 'ລາຄາ', 'ຈຳນວນ', 'ລວມ']
resulttable = ttk.Treeview(T2, columns=header, show='headings', height=10)
resulttable.pack()
# for i in range(len(header)):
#     resulttable.heading(header[i], text=header[i])
for i in header:
    resulttable.heading(i, text=i)
headerwidth = [90, 70, 120, 50, 50, 70]
for i, j in zip(header, headerwidth):
    resulttable.column(i, width=j)

# resulttable.insert('', 'end',value['Mon-20-2020','pen','20','5','100'] ) # end is an index of data
# resulttable.insert('', 0,,value['Mon-20-2020','pen','20','5','100'] )

F2 = Frame(T2)
F2.pack(pady=5)

transactions = {}  # create transaction id for update or delete records


def UpdateCSV():
    with open('expense.csv', 'w', newline='', encoding='utf-8') as f:
        fw = csv.writer(f)
        data = list(transactions.values())
        fw.writerows(data)
        # print('table update to date')

def UpdateSQL():
    data = list(transactions.values())
    for d in data:
        update_expense(d[0], d[2], d[3], d[4], d[5])


def DeleteRecord(event=None):
    check = messagebox.askyesno('Confirm', 'Do you really want to delete record from db?')
    if check == True:
        select = resulttable.selection()
        data = resulttable.item(select)
        transactionId = data['values'][0]
        # print('DeleteRecord', transactionId)
        # del transactions[str(transactionId)]
        # # UpdateCSV()
        delete_expense(str(transactionId))
        UpdateTable()
        # print('record updated')


B3 = ttk.Button(F2, text='Delete', command=DeleteRecord)
B3.grid(row=0, column=0)

resulttable.bind('<Delete>', DeleteRecord)

def UpdateRecord():
    select = resulttable.selection()
    data = resulttable.item(select)
    pass

def UpdateTable():
    try:
        # for c in resulttable.get_children():
        #     resulttable.delete(c)
        resulttable.delete(*resulttable.get_children())
        # data = ReadCSV()
        data = show_expense()
        # print(data)
        for d in data:
            resulttable.insert('', 0, value=d[1:])
            # print('UpdateTable', d)
            transactions[d[1]] = d[1:]  # create transaction id for update or delete records
        # print('UpdateTableTransactions', transactions)
    except:
        print('No DB found')

# right click menu
def EditRecord():
    popup = Toplevel()
    popup.geometry('500x400+400+50')
    popup.title('Edit Record')
    L = ttk.Label(popup, text='Expense item', font=FONT1).pack()

    v_expense = StringVar()
    E5 = ttk.Entry(popup, textvariable=v_expense, font=FONT1)
    E5.pack()

    L = ttk.Label(popup, text='Price', font=FONT1).pack()
    v_price = StringVar()
    E6 = ttk.Entry(popup, textvariable=v_price, font=FONT1)
    E6.pack()

    L = ttk.Label(popup, text='Amount', font=FONT1).pack()
    v_amount = StringVar()
    E7 = ttk.Entry(popup, textvariable=v_amount, font=FONT1)
    E7.pack()

    def Edit():
        # print('EDITID', editId)
        # print('TRANSACTIONS', transactions)
        olddata = transactions[str(editId)]
        # print('OLD', olddata)
        v1 = v_expense.get()
        v2 = float(v_price.get())
        v3 = float(v_amount.get())
        total = v2 * v3
        newdata = [olddata[0], olddata[1], v1, v2, v3, total]
        transactions[str(editId)] = newdata
        # UpdateCSV()
        UpdateSQL()
        UpdateTable()
        popup.destroy()

    icon_3 = PhotoImage(file='asset/save.png')
    B5 = ttk.Button(popup, text='- Save -', command=Edit, image=icon_3, compound='left')
    B5.pack(ipadx=15, ipady=10, pady=5)

    select = resulttable.selection()
    data = resulttable.item(select)
    editItem = data['values']
    editId = data['values'][0]
    # print('selecteditdata', data)
    v_expense.set(editItem[2])
    v_price.set(editItem[3])
    v_amount.set(editItem[4])
    
    popup.mainloop()

B4 = ttk.Button(F2, text='Edit', command=EditRecord)
B4.grid(row=0, column=1)

rightclick = Menu(GUI, tearoff=0)
rightclick.add_command(label='Edit', command=EditRecord)
rightclick.add_command(label='Delete', command=DeleteRecord)

def PopUpMenu(event):
    # print(event.x_root, event.y_root)
    rightclick.post(event.x_root, event.y_root)

resulttable.bind('<Button-2>', PopUpMenu) ## for windows use <Button-3> for right click

UpdateTable()

GUI.mainloop()
