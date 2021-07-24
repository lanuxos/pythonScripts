# EP.1 - TRANSLATOR APP
from tkinter import *
from tkinter import ttk
from googletrans import Translator

translator = Translator()

GUI = Tk()
GUI.geometry('500x300')
GUI.title('Translator using Googletrans python package')

FONT = ('Times New Roman', 15)

L = Label(GUI, text='Type word(s) you wanna translate below:')
L.pack()

v_vocab = StringVar()

E1 = Entry(GUI, textvariable=v_vocab, font=FONT, width=40)
E1.pack(pady=10)

def Translate():
    vocab = v_vocab.get()
    meaning = translator.translate(vocab, dest='th')
    v_result.set(vocab + ' : ' + meaning.text + ' [' + meaning.pronunciation + ' ]')
    print(vocab, meaning.text, meaning.pronunciation)

B1 = Button(GUI, text='Translate >>>', command=Translate)
B1.pack(ipadx=20, ipady=10)

L = Label(GUI, text='Meaning', font=FONT, width=20)
L.pack(ipady=10)

v_result = StringVar()
R1 = Label(GUI, textvariable=v_result, font=FONT, width=50, foreground='green')
R1.pack(ipady=20)

B2 = Button(GUI, text='</Exit>', command=GUI.destroy)
B2.pack(ipadx=20, ipady=10)

GUI.mainloop()
