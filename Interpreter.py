# repeat <список операторів> until <лог. вираз> if <лог. вираз> goto <мітка>
# +-*/↑, унарний мінус, (), цілі константи

from tkinter import *
from tkinter.ttk import *

import LexicalAnalyzer
import SyntaxAnalyzer
import PolishCodeGenerator
import PolishCodeInterpreter

tk = Tk()
line1 = Frame(tk)
line1.pack(fill=X)
line2 = Frame(tk)
line2.pack(fill=X)
line3 = Frame(tk)
line3.pack(fill=X)

codeArea = Text(line1, borderwidth=3, relief="sunken")
codeArea.config(font=("consolas", 12), undo=True, wrap='word')
codeArea.pack(side=LEFT)

index = 1
with open("code.txt") as file:
    for line in file.readlines():
        codeArea.insert(str(index) + ".0", line)
        index += 1

scroll = Scrollbar(line1, command=codeArea.yview)
scroll.pack(side=LEFT, fill=Y)
codeArea['yscrollcommand'] = scroll.set

tabControl = Notebook(line1)
tab1 = Frame(tabControl)
tabControl.add(tab1, text='Таблица лексем')
tab2 = Frame(tabControl)
tabControl.add(tab2, text='Таблица переменных')
tab3 = Frame(tabControl)
tabControl.add(tab3, text='Таблица констант')
tabControl.pack(expand=1, fill=BOTH)

Output_text = ""

def lexicalAnalysis():
    global tab1, tab2, tab3, text2

    tab1.destroy()
    tab1 = Frame(tabControl)
    tabControl.add(tab1, text='Таблица лексем')
    tab2.destroy()
    tab2 = Frame(tabControl)
    tabControl.add(tab2, text='Таблица переменных')
    tab3.destroy()
    tab3 = Frame(tabControl)
    tabControl.add(tab3, text='Таблица констант')

    code = codeArea.get("0.0", END)
    lex_list, var_list, con_list = LexicalAnalyzer.analyze(code)

    try:
        SyntaxAnalyzer.analyze(lex_list, var_list, con_list)
        poliz_list = PolishCodeGenerator.generatePOLIZ(lex_list, var_list, con_list)
        for element in poliz_list:
            print(element[1] + " ", end="")
        Output_text = PolishCodeInterpreter.run(poliz_list, lex_list, var_list, con_list)
    except Exception as e:
        Output_text = "Line " + str(e)
        raise e

    text2.config(state=NORMAL)
    text2.delete(1.0, END)
    text2.insert("1.0", Output_text)
    text2.config(state=DISABLED)

    table = Treeview(tab1, selectmode="browse")
    table["columns"] = ("one", "two", "three")
    table.column("#0", width=0, minwidth=0, stretch=NO)
    table.column("one", width=40, minwidth=40)
    table.column("two", width=30, minwidth=30)
    table.column("three", width=10, minwidth=10)
    table.heading("one", text="Line", anchor=W)
    table.heading("two", text="Type", anchor=W)
    table.heading("three", text="Table number", anchor=W)

    for row in lex_list:
        table.insert('', END, values=tuple(row))

    scrolltable = Scrollbar(tab1, command=table.yview)
    table.configure(yscrollcommand=scrolltable.set)
    scrolltable.pack(side=RIGHT, fill=Y)
    table.pack(expand=YES, fill=BOTH)

    table = Treeview(tab2, selectmode="browse")
    table["columns"] = ("one", "two", "three")
    table.column("#0", width=0, minwidth=0, stretch=NO)
    table.column("one", width=40, minwidth=40)
    table.column("two", width=30, minwidth=30)
    table.column("three", width=10, minwidth=10)
    table.heading("one", text="Index", anchor=W)
    table.heading("two", text="Name", anchor=W)
    table.heading("three", text="Value", anchor=W)

    for row in var_list:
        table.insert('', END, values=(var_list.index(row), row[0], row[1]))

    scrolltable = Scrollbar(tab2, command=table.yview)
    table.configure(yscrollcommand=scrolltable.set)
    scrolltable.pack(side=RIGHT, fill=Y)
    table.pack(expand=YES, fill=BOTH)

    table = Treeview(tab3, selectmode="browse")
    table["columns"] = ("one", "two")
    table.column("#0", width=0, minwidth=0, stretch=NO)
    table.column("one", width=40, minwidth=40)
    table.column("two", width=30, minwidth=30)
    table.heading("one", text="Index", anchor=W)
    table.heading("two", text="Value", anchor=W)

    for row in con_list:
        table.insert('', END, values=(con_list.index(row), row))

    scrolltable = Scrollbar(tab3, command=table.yview)
    table.configure(yscrollcommand=scrolltable.set)
    scrolltable.pack(side=RIGHT, fill=Y)
    table.pack(expand=YES, fill=BOTH)


text2 = Text(line2, borderwidth=1, relief="sunken")
scroll2 = Scrollbar(line2, command=text2.yview)
scroll2.pack(side=RIGHT, fill=Y)
text2['yscrollcommand'] = scroll2.set
text2.config(font=("consolas", 12), undo=False, wrap='word', height=10, state=DISABLED)
text2.pack(fill=X)

button = Button(line3, text="RUN", command=lexicalAnalysis)
button.pack(side=BOTTOM, fill=X)

tk.mainloop()
