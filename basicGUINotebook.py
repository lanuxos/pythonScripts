# EP.1 Basic GUI

from tkinter import *
from tkinter import ttk, messagebox
import csv, random

def WriteToCSV(data):
    with open('ep2.csv', 'a', newline='', encoding='utf-8') as file:  # a - append, w - write
        fw = csv.writer(file)
        fw.writerow(data)
    print('Saved')

def ReadCSV():
    with open('ep2.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        # print(data)
        return data

def UpdateTable():
    table.delete(*table.get_children())
    alldata = ReadCSV()
    for row in alldata:
        table.insert('', 'end', value=row)

def SaveButton(event=None):
    title = v_title.get()
    detail = v_detail.get()
    print(title, detail)
    dt = [title, detail]
    WriteToCSV(dt)
    print('Your data saved...')
    UpdateTable()
    v_title.set('')
    v_detail.set('')
    e1.focus()
    global allquestion
    allquestion = ReadCSV()

def DeleteQuestion(event=None):
    select = table.selection()
    data = table.item(select)
    # print(data['values'])
    allquestion.remove(data['values'])
    # print(len(allquestion))
    table.delete(*table.get_children())
    alldata = allquestion
    for row in alldata:
        table.insert('', 'end', value=row)

def SaveQuestion(event=None):
    check = messagebox.askquestion('Confirm', 'Do you really want to save the current data?')
    if check == 'yes':
        with open('ep2.csv', 'w', newline='', encoding='utf-8') as file:
            fw = csv.writer(file)
            fw.writerows(allquestion)
        messagebox.showinfo('saving...', 'Save change to database')

root = Tk()
root.title('Basic GUI')
root.geometry('500x500')
font1 = ('Times New Roman', 15, 'bold')
font2 = ('Defago Noto Sans', 15)

root.bind('<F1>', SaveQuestion)

tab = ttk.Notebook(root)

t1 = Frame(tab)
t2 = Frame(tab)

tab.add(t1, text='Add')
tab.add(t2, text='Flash Card')
tab.pack(fill=BOTH, expand=1)

l = ttk.Label(t1, text='To save new database press <F1>')
l.pack()

l1 = Label(t1, text='Title', font=font2, fg='purple', width=20)
l1.pack(ipadx=5)

v_title = StringVar()
e1 = Entry(t1, font=font2, fg='green', textvariable=v_title)
e1.pack(ipadx=5, ipady=5)
e1.focus()

l2 = Label(t1, text="Detail", font=font2, fg='purple', width=30)
l2.pack(ipadx=5)

v_detail = StringVar()
e2 = Entry(t1, font=font2, fg='green', textvariable=v_detail)
e2.pack(ipadx=5, ipady=5)

b1 = ttk.Button(t1, text="Save", command=SaveButton)
b1.pack(ipadx=5, ipady=5, pady=10)

style = ttk.Style()
style.configure('Treeview.Heading', font=('Defago Noto Sans', 12))
style.configure('Treeview', font=('Defago Noto Sans', 12), rowheight=30)

header = ['Title', 'Detail']

table = ttk.Treeview(t1, height=10, column=header, show='headings')
table.place(x=100, y=250)

table.heading('Title', text='Title')
table.column('Title', width=120)
table.heading('Detail', text='Detail')
table.column('Detail', width=165)

table.bind('<Delete>', DeleteQuestion)
'''
# TO MANUAL INSERT DATA INTO TREEVIEW
row = ['Title1', 'Detail1']
table.insert('', 'end', value=row)
'''

UpdateTable()

allquestion = ReadCSV()
v_current_ans = StringVar()
def Next():
    q = random.choice(allquestion)
    v_question.set(q[0])
    v_current_ans.set(q[1])
    v_answer.set('-=Press Show to display the answer=-')
    bc3['state'] = 'enabled'

def Show():
    v_answer.set(v_current_ans.get())

v_score = StringVar()
init=0
v_score.set('Score: {}'.format(init))
def ScoreUp():
    global init
    init += 1
    v_score.set('Score: {}'.format(init))
    bc3['state'] = 'disabled'

v_question = StringVar()
v_question.set('-=Question to continue, press Next=-')
r1 = ttk.Label(t2, textvariable=v_question, font=font1)
r1.pack(pady=100)
v_answer = StringVar()
v_answer.set('-=Press Show to display the answer=-')
r2 = ttk.Label(t2, textvariable=v_answer, font=font1)
r2.pack(pady=50)

bf1 = Frame(t2)
bf1.pack(pady=50)

bc1 = ttk.Button(bf1, text='Next', command=Next)
bc2 = ttk.Button(bf1, text='Show', command=Show)
bc3 = ttk.Button(bf1, text='Score +1', command=ScoreUp)
bc1.grid(row=0, column=0)
bc2.grid(row=0, column=1)
bc3.grid(row=0, column=2)

score = ttk.Label(t2, textvariable=v_score, font=font1)
score.place(x=400, y=20)

e2.bind('<Return>', SaveButton)
root.bind('<Escape>', lambda x: root.destroy())
root.mainloop()
