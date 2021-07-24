# Basic Python ReportLab
# pip install reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from subprocess import Popen
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph

pdfmetrics.registerFont(TTFont('laofont','Defago.ttf'))

c = canvas.Canvas('hello.pdf', pagesize=A4)
def Text(c, x,y,text='ReportLab', font='laofont', size=15, color=colors.black):
	c.setFont(font, size)
	c.setFillColor(color)
	c.drawCentredString(x, y, text)

# Text(c, 105*mm,285*mm, 'ສະບາຍດີ ReportLab')
# Text(c, 105*mm,297/2*mm, 'ສະບາຍດີ ReportLab', color=colors.green)

textlines = ['Line 1', 'Line 2', 'Line 3']

text = c.beginText(100*mm, 260*mm)
text.setFont('laofont', 15)
text.setFillColor(colors.green)

for line in textlines:
	text.textLine(line)
c.drawText(text)

c.showPage()
c.save()

# Popen('hello.pdf', shell=True)
