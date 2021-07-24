# EP.1 Basic GUI

from tkinter import *
from tkinter import ttk
import csv

def WriteToCSV(data):
    with open('ep2.csv', 'a', newline='', encoding='utf-8') as file:  # a - append, w - write
        fw = csv.writer(file)
        fw.writerow(data)
    print('Saved')

def ReadCSV():
    with open('ep2.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        # print(data)
        return data

def UpdateTable():
    table.delete(*table.get_children())
    alldata = ReadCSV()
    for row in alldata:
        table.insert('', 'end', value=row)

def SaveButton(event=None):
    title = v_title.get()
    detail = v_detail.get()
    print(title, detail)
    dt = [title, detail]
    WriteToCSV(dt)
    print('Your data saved...')
    UpdateTable()
    v_title.set('')
    v_detail.set('')
    e1.focus()

root = Tk()
root.title('Basic GUI')
root.geometry('500x500')
font1 = ('Times New Roman', 15, 'bold')
font2 = ('Defago Noto Sans', 15)

l0 = Label(root, text="Basic GUI", font=font1, fg='purple')
l0.pack(ipadx=5, ipady=5)

l1 = Label(root, text='Title', font=font2, fg='purple', width=20)
l1.pack(ipadx=5, ipady=5)

v_title = StringVar()
e1 = Entry(root, font=font2, fg='green', textvariable=v_title)
e1.pack(ipadx=5, ipady=5)
e1.focus()

l2 = Label(root, text="Detail", font=font2, fg='purple', width=30)
l2.pack(ipadx=5, ipady=5)

v_detail = StringVar()
e2 = Entry(root, font=font2, fg='green', textvariable=v_detail)
e2.pack(ipadx=5, ipady=5)

b1 = ttk.Button(root, text="Save", command=SaveButton)
b1.pack(ipadx=5, ipady=5, pady=5)

header = ['Title', 'Detail']

table = ttk.Treeview(root, height=10, column=header, show='headings')
table.place(x=100, y=275)

table.heading('Title', text='Title')
table.column('Title', width=120)
table.heading('Detail', text='Detail')
table.column('Detail', width=165)

'''
# TO MANUAL INSERT DATA INTO TREEVIEW
row = ['Title1', 'Detail1']
table.insert('', 'end', value=row)
'''

UpdateTable()

e2.bind('<Return>', SaveButton)
root.bind('<Escape>', lambda x: root.destroy())
root.mainloop()
