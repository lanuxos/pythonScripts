# EP.4 OCR - Pytesseract
from PIL import Image
import pytesseract, csv

# print(pytesseract.image_to_string(Image.open('../asset/book2.jpg')))
# print('--------------------------------')
# print(pytesseract.image_to_string(Image.open('../asset/book.jpg'), lang='tha'))
# print('--------------------------------')
# print('--------------------------------')
# print(pytesseract.image_to_string(Image.open('../asset/book.jpg'), lang='chi_sim'))
# var = [pytesseract.image_to_string(Image.open('../asset/oil.jpg'), lang='lao')]
data=pytesseract.image_to_string(Image.open('../asset/oil.jpg'), lang='Laos')

# print('-----')
# print(type(vars))

# write to csv
def Write(data):
	with open('../asset/ocrOutput.csv', 'a', newline='', encoding='utf-8') as file:  # a - append, w - write
	    fw = csv.writer(file)
	    fw.writerow(data)
	    # print('Saved')

nl = data.split('\n')
price=[]
for n in nl:
	if len(list(n))>57:
		p = n.replace('|','')
		l = p.split(' ')[-7:]
		if len(l[1]) > 0:
			price.append({'pro':l[0],'old95':l[1],'new95':l[2],'old91':l[3],'new91':l[4],'olddie':l[5],'newdie':l[6]})
for p in price:
	print(p)			