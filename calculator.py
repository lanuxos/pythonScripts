# HOMEWORK

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x300')
root.title('Calculator')

f = Frame(root)
f.pack(ipadx=10, ipady=10)
ff = Frame(root)
ff.pack(ipadx=10, ipady=20)
fff = Frame(root)
fff.pack(ipadx=10, ipady=20)

v_product = StringVar()
v_price = IntVar()
v_amount = IntVar()
v_total = StringVar()
v_totalvat = StringVar()

l = Label(f, text='Calculate the product price plus 7% vat').grid(row=0, columnspan=2)

l1 = Label(f, text='Product Name:')
l1.grid(row=1, column=0)
e1 = Entry(f, textvariable=v_product)
e1.grid(row=1, column=1)
e1.focus()

l2 = Label(f, text='Product Price:')
l2.grid(row=2, column=0)
e2 = Entry(f, textvariable=v_price)
e2.grid(row=2, column=1)

l3 = Label(f, text='Product Amount:')
l3.grid(row=3, column=0)
e3 = Entry(f, textvariable=v_amount)
e3.grid(row=3, column=1)

def Calc(event=None):
    if v_product.get() == '':
        product = '<N/A>'
    else:
        product = v_product.get()
    price = v_price.get()
    amount = v_amount.get()
    t = (price * amount) + ((price * amount) * 7 / 100)
    tv = (price * amount) 
    v_total.set(f'{product} : {t:,.2f}')
    v_totalvat.set(f'{product} : {tv:,.2f}')
    print(product, price, amount, t, tv)

root.bind('<Return>', Calc)
root.bind('<Escape>', lambda x: root.destroy())

b1 = ttk.Button(ff, text='Calc Now', command=Calc, width=10).grid(row=5,column=0)
b2 = ttk.Button(ff, text='Exit Now', command=root.destroy, width=10).grid(row=5,column=1)

l4 = Label(fff, text="Total w/o vat:", width=20, justify=RIGHT).grid(row=6, column=0)
l5 = Label(fff, textvariable=v_total, width=20, justify=LEFT).grid(row=6, column=1)
l6 = Label(fff, text="Total + 7% vat:", width=20, justify=RIGHT).grid(row=7, column=0)
l7 = Label(fff, textvariable=v_totalvat, width=20, justify=LEFT).grid(row=7, column=1)

root.mainloop()
