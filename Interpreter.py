from tkinter import *

tk = Tk()
line1 = Frame(tk)
line1.pack()

text = Text(line1, borderwidth=3, relief="sunken")
text.config(font=("consolas", 12), undo=True, wrap='word')
text.pack(side=LEFT)

scroll = Scrollbar(line1, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text['yscrollcommand'] = scroll.set

label = Label(line1, text="HELLO", width=100);
label.pack(side=LEFT)

button = Button(tk, text="RUN")
button.pack(fill=X)

tk.mainloop()