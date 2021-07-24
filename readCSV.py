# Read CSV

import csv
import os
print(os.listdir())

def ReadCSV():
	with open('ep2.csv', newline='', encoding='utf-8') as file:
		fr = csv.reader(file)
		data = list(fr)
		# print(data)
		return data

alldata = ReadCSV()
for a in alldata:
	print(a)