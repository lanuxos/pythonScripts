# EP.4 - WORKING WITH EXCEL
# pip install openpyxl

from googletrans import Translator
from openpyxl import Workbook
from datetime import datetime

t = Translator()

article = open('ep3.article.txt', 'r')
article = article.read()
article = article.split()

result = []
for word in article:
    res = t.translate(word, dest='th')
    if res != None:
        result.append([word, res.text])

excelfile = Workbook()
sheet = excelfile.active

header = ['Vocabuary', 'Trabslate']
sheet.append(header)

for rs in result:
    sheet.append(rs)
dt = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
excelfile.save(f'{dt}-excelTrans.xlsx')