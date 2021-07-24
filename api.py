# EP.6 API
import requests, time
from pprint import pprint

api_url = 'https://api.bitkub.com'

endpoint = {
	'status':'/api/status',
	'timestamp':'/api/servertime',
	'symbols':'/api/market/symbols',
	'ticker':'/api/market/ticker',
	'trades':'/api/market/trades',
}

def Status():
	url = api_url + endpoint['status']
	r = requests.get(url)
	if r.status_code == 200:
		print('Server response correctly')
	return r.status_code

def ServerTime():
	url = api_url + endpoint['timestamp']
	localtime = time.time()
	r = requests.get(url)
	data = r.json()
	print(time.ctime(localtime))
	print(time.ctime(data))

def AllSymbol():
	url = api_url + endpoint['symbols']
	r = requests.get(url)
	# pprint(r.json())
	data = r.json()
	pprint(data['result'])

def Ticker(coin = 'THB_BTC', whole = False):
	url = api_url + endpoint['ticker']
	if whole == True:
		r = requests.get(url)
		data = r.json()
		pprint(data)
		return data
	else:
		r = requests.get(url, params={'sym': coin})
		data = r.json()
		pprint(data)
		print('----')
		print(data[coin].get('last'))
		print(data[coin].get('percentChange'))
		return data

def Trades():
	url = api_url + endpoint['trades']
	r = requests.get(url)
	data = r.json()
	return data
# Status()
# ServerTime()
# AllSymbol()
Ticker(coin = 'THB_BTC')