# EP.6 API
import requests
from bs4 import BeautifulSoup

def Oil():
	url = 'https://www.shell.co.th/th_th/motorists/shell-fuels/fuel-price/app-fuel-prices.html'
	rawdata = requests.get(url)
	rawdata = rawdata.content
	data = BeautifulSoup(rawdata, 'html.parser')

	oil = data.find('table', {'class':'cc_cursor'})
	# print(oil.find_all('tr')[2].text)
	result = ''
	for o in oil.find_all('tr')[1:]:
		text = o.text.strip()
		# print(text)
		result += text + '\n'
	return result

print(Oil())