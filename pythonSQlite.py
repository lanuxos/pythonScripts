# Basic python with SQlite
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3, random

def Save(event=None):
    global addV
    v = vocab.get()
    d = desc.get()
    print(v, ": ", d)
    if len(v) > 0 and len(d) > 0:
        Insert(v, d)
        vocab.set('')
        desc.set('')
        e1.focus()
        table1.delete(*table1.get_children())
        addV = View()
        for v in addV:
            table1.insert('','end',value=v)
    else:
        messagebox.showinfo('Attention', 'Please enter some words or phases to save into db')

conn = sqlite3.connect('vocabs.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS vocab (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vocab text,
    desc text, 
    score int
)""" )

def Insert(voc, des):
    id = None
    score = 0
    with conn:
        c.execute("""INSERT INTO vocab VALUES (?,?,?,?)""", (id, voc, des, score))
    conn.commit()
    print('>>> Saved ::..')

def View():
    with conn:
        c.execute("SELECT * FROM vocab")
        vocabs = c.fetchall()
        # print(vocabs)
    return vocabs

root = Tk()
root.geometry('500x300+400+200')
root.title('Python with SQlite DB')

lao = ('Defago Noto Sans', 15)
english = ('Times New Roman', 15)

tab = ttk.Notebook(root)
t1 = Frame(tab)
t2 = Frame(tab)
t3 = Frame(tab)
tab.add(t1, text='Add DB')
tab.add(t2, text='Show DB')
tab.add(t3, text='Play')
tab.pack(fill=BOTH, expand=1)

l1 = Label(t1, text='Vocabs')
l1.pack(pady=5)
vocab = StringVar()
e1 = ttk.Entry(t1, textvariable=vocab, font=english)
e1.pack(pady=2)
e1.focus()
l2 = Label(t1, text='Desc')
l2.pack(pady=5)
desc = StringVar()
e2 = ttk.Entry(t1, textvariable=desc, font=lao)
e2.pack(pady=2)
b1 = ttk.Button(t1, text="Save To DB", command=Save)
b1.pack(pady=5)

######################

header = ['id', 'vocab', 'desc', 'score']
headsize= [20,120,220,40]
table1 = ttk.Treeview(t2, columns=header, show='headings', height=10)
table1.place(x=20, y=20)

for h, s in zip(header, headsize):
    table1.heading(h, text=h)
    table1.column(h, width=s)

addV = View()

if len(addV) > 0:
    for v in addV:
        table1.insert('','end',value=v)

######################

currentResult = []

def Next():
    global currentResult
    current = random.choice(addV)
    currentResult = current
    result0.set(current[1])
    result1.set('Desc display box')

def Show():
    result1.set(currentResult[2])
result0 = StringVar()
result0.set('Vocab display box')
result1 = StringVar()
result1.set('Desc display box')

l3 = Label(t3, textvariable=result0, font=english).pack(pady=10)
l4 = Label(t3, textvariable=result1, font=english).pack(pady=10)

f = Frame(t3)
f.pack(pady=10)
b2 = ttk.Button(f, text="Next Vocab", command=Next)
b2.grid(row=0, column=0)
b3 = ttk.Button(f, text="Show Desc", command=Show)
b3.grid(row=0, column=1)

addV = View()

e2.bind('<Return>', Save)
root.bind('<Escape>', lambda x:root.destroy())

root.mainloop()