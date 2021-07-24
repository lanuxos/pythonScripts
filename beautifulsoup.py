# EP.5 Basic webscraping
# pip install beautifusoup requests
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

print(CheckRate('THB'))