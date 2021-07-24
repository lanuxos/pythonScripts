# EP.5 Check exchange rate
# pip install beautifusoup requests
from tkinter import *
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup

def CheckRate(code='USD 1-20'):
	url = 'https://bcel.com.la/bcel/exchange-rate.html'

	rawdata = requests.get(url)
	rawdata = rawdata.content

	data = BeautifulSoup(rawdata, 'html.parser')
	currency = data.find_all('td', {'data-title':'ປະເພດສະກຸນເງິນ'})
	codes = data.find_all('td', {'data-title':'ລະຫັດສະກຸນເງິນ'})
	sell = data.find_all('td', {'data-title':'ອັດຕາຂາຍ'})
	# print(sell)
	result = []
	for cu, co, ra in zip(currency, codes, sell):
		# print(f'{cu.text.strip()} [{co.text.strip()}] {ra.text.strip()}')
		# print('-----')
		# print(co.text.strip())
		if co.text.strip() == code:
			result.append({'currency':cu.text.strip(), 'codes':co.text.strip(), 'sell':ra.text.strip()})
	return result

# print(CheckRate('THB'))

root = Tk()
root.geometry('300x200')
root.title('Exchange Rate _refer to BCEL')
root.iconbitmap('ep5.ico')

f = ('Times New Roman', 12)
f1 = ('Defago Noto Sans', 12)

img = PhotoImage(file='ep5.png')

l0 = ttk.Label(root, image=img).pack(pady=5)

l1 = ttk.Label(root, text='Choose your destinate currency below', font=f)
l1.pack(pady=5)

fr1 = ttk.Frame(root)
fr1.pack(pady=5)
v_result = StringVar()
v_result.set('xxx')

def Selected():
	val = v_radio.get()
	res = CheckRate(val)
	res = res[0]['sell']
	res = f'{res} ກີບ'
	# print(res[0]['sell'])
	v_result.set(res)

v_radio = StringVar()
r1 = ttk.Radiobutton(fr1, text='USD 1-20', value='USD 1-20', variable = v_radio, command=Selected, width=10)
r1.grid(row=2, column=0)
r2 = ttk.Radiobutton(fr1, text='THB', value='THB', variable = v_radio, command=Selected, width=10)
r2.grid(row=2, column=2)
r3 = ttk.Radiobutton(fr1, text='VND', value='VND', variable = v_radio, command=Selected, width=10)
r3.grid(row=2, column=4)

# v_amount = StringVar()
# v_amount.set(1)
# e1 = ttk.Entry(root, textvariable = v_amount, font=f, justify='center')
# e1.pack(pady=5)

# def Calc():
# 	amount = float(v_amount.get())
# 	if v_radio.get() == '':
# 		r1.invoke()
# 		# messagebox.showinfo('Check Input', 'Please select the currency you want to convert')
# 	else:	
# 		val = v_radio.get()
# 		res = CheckRate(val)
# 		res = res[0]['sell'].replace('.','')
# 		print(res)
# 		res = float(res)
# 		res *= amount
# 		# print(res)
# 		# res = float(res) * float(amount)
# 		# res = f'{res} ກີບ'
# 		# # print(res[0]['sell'])
# 		v_result.set(res)

# b1 = ttk.Button(root, text='Calc', command=Calc)
# b1.pack(pady=5)

fr2 = ttk.Frame(root)
fr2.pack(pady=5)

l2 = ttk.Label(fr2, text='Exchange rate: ', font=f)
l2.grid(row=7, column=0)

l3 = ttk.Label(fr2, font=f1, textvariable=v_result)
l3.grid(row = 7, column=1, columnspan=3)

statusbar = Label(root, text='This exchange rate is refered from BCEL daily rate')
statusbar.pack(side=BOTTOM)

root.bind('<Escape>', lambda x: root.destroy())

root.mainloop()