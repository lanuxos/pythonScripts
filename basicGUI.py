# EP.1 Basic GUI

from tkinter import *
from tkinter import ttk
import csv

root = Tk()
root.title('Basic GUI')
root.geometry('500x300')
font1 = ('Times New Roman', 15, 'bold')
font2 = ('Defago Noto Sans', 15)

l0 = Label(root, text="Basic GUI", font=font1, fg='purple')
l0.pack(ipadx=5, ipady=10)

l1 = Label(root, text='Title', font=font1, fg='purple', width=20)
l1.pack(ipadx=5, ipady=5)

v_title = StringVar()
e1 = Entry(root, font=font2, fg='green', textvariable=v_title)
e1.pack(ipadx=10, ipady=10)
e1.focus()

l2 = Label(root, text="Detail", font=font1, fg='purple', width=30)
l2.pack(ipadx=5, ipady=5)

v_detail = StringVar()
e2 = Entry(root, font=font2, fg='green', textvariable=v_detail)
e2.pack(ipadx=10, ipady=10)

def WriteToCSV(data):
    with open('test.csv', 'a', newline='', encoding='utf-8') as file:  # a - append, w - write
        fw = csv.writer(file)
        fw.writerow(data)
    print('Saved')

def SaveButton(event=None):
    title = v_title.get()
    detail = v_detail.get()
    print(title, detail)
    dt = [title, detail]
    WriteToCSV(dt)
    print('Your data saved...')
    v_title.set('')
    v_detail.set('')
    e1.focus()

b1 = ttk.Button(root, text="Save", command=SaveButton)
b1.pack(ipadx=10, ipady=10, pady=10)

e2.bind('<Return>', SaveButton)
root.bind('<Escape>',lambda x: root.destroy())
root.mainloop()
