# binance api gui
# https://www.youtube.com/watch?v=I4mO5pWSNaA&t=5s
apiKey = 'EjFmmQoUA3hXQhKjwgFjgqf3F7YycRmFLCrEMSnzmRQbxGASVo47mU4BvDhuAxEz'
secretKey = '8RZ3YczxPqT3hFEEpqyVwNaH6hofn1DxTX6Yxvpn8I769L86dizv9p6Tub1ijpVu'
import time
from time import mktime
from datetime import datetime, timedelta
from pprint import pprint
from binance.client import Client
from tkinter import *
from tkinter import ttk, messagebox

client = Client(apiKey, secretKey)

time_res = client.get_server_time() # milliseconds
# print('>SERVER_TIME_IN_MILLISECONDS', time_res['serverTime'])
seconds = time_res['serverTime'] / 1000
# print('>SERVER_TIME_WITH_CTIME', time.ctime(seconds))
# print('>SERVER_TIME_IN_LOCAL', time.localtime(seconds))
dt = datetime.fromtimestamp(mktime(time.localtime(seconds)))
dt = dt.strftime('%Y-%m-%d %H:%M:%S')
print('>SERVER_TIME_LOCAL_COMPUTER_TIME', dt)

def CheckPrice():    
    price = client.get_all_tickers()
    coin_name = 'DOGEUSDT'
    current_price = ''
    for p in price:
        if p['symbol'] == coin_name:
            current_price = p
            # print(current_price)
            time.sleep(0.5)
            v_balance.set(current_price['symbol'])
            v_price.set(current_price['price'])
            root.after(100, CheckPrice)

root = Tk()
root.geometry('500x300')
root.title('Binance API GUI with Tkinter')

englist = ('Times New Roman', 25)

f1 = Frame(root)
f1.pack(pady=5)

v_balance = StringVar()
v_balance.set('-')
v_price = StringVar()
v_price.set('-')

lBalance = Label(root, textvariable=v_balance).pack()
lPrice = Label(root, textvariable=v_price).pack()

CheckPrice()

root.bind('<Escape>', lambda x:root.destroy())
root.mainloop()
