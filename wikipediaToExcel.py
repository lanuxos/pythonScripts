# EP.4 Excel Automation
from openpyxl import Workbook
import wikipedia

wikipedia.set_lang('th')
product = ['computer mouse', 'computer keyboard']

excelfile = Workbook()
sheet = excelfile.active

sheet['B1'] = 'Product List'
header = ['No', 'Product', 'Price', 'Detail']
sheet.append(header)

for i, pd in enumerate(product):
    content = wikipedia.summary(pd)
    row = [i + 1, pd, 100, content]
    sheet.append(row)

excelfile.save('../asset/wikipediatoexcel.xlsx')