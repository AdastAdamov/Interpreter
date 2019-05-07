from tkinter import *
from tkinter.ttk import Notebook

tk = Tk()
line1 = Frame(tk)
line1.pack()
line2 = Frame(tk)
line2.pack(fill=X)
line3 = Frame(tk)
line3.pack(fill=X)

text = Text(line1, borderwidth=3, relief="sunken")
text.config(font=("consolas", 12), undo=True, wrap='word')
text.pack(side=LEFT)
scroll = Scrollbar(line1, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text['yscrollcommand'] = scroll.set

tabControl = Notebook(line1)
tab1 = Frame(tabControl)
tabControl.add(tab1, text='Таблица лексем')
tab2 = Frame(tabControl)
tabControl.add(tab2, text='Таблица переменных')
tabControl.pack(expand=1, fill="both")

label = Label(tab1, text="HELLO", width=50);
label.pack(side=LEFT)

text2 = Text(line2, borderwidth=1, relief="sunken")
scroll2 = Scrollbar(line2, command=text2.yview)
scroll2.pack(side=RIGHT, fill=Y)
text2['yscrollcommand'] = scroll2.set
text2.config(font=("consolas", 12), undo=False, wrap='word', height=10, state=DISABLED)
text2.pack(fill=X)

button = Button(line3, text="RUN")
button.pack(side=BOTTOM, fill=X)

tk.mainloop()
