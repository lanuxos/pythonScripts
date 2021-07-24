# EP.1 Write CSV
import csv

def WriteToCSV(data):
    with open('test.csv', 'a', newline='', encoding='utf-8') as file:  # a - append, w - write
        fw = csv.writer(file)
        fw.writerow(data)
    print('Saved')

dt = ['Test', 'To', 'Save', 'List', 'To', 'CSV', 'file']
WriteToCSV(dt)