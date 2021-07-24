# EP.6 API
import requests
from bs4 import BeautifulSoup

province = {'BBK':'48455', 'XM':'48327'}

def Temp(name):
	url = 'https://www.tmd.go.th/province.php?StationNumber={}'.format(province[name])
	rawdata = requests.get(url)
	rawdata = rawdata.content
	data = BeautifulSoup(rawdata, 'html.parser')

	temp = data.find('td', {'class':'strokeme'})
	pvname = data.find('span', {'class':'title'})
	print(pvname.text, temp.text)

Temp('XM')