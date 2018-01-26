'''
May 25,  2015
Recipe:  B04829_01_08
@author: Burkhard Meier
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import Radiobutton
from tkinter import scrolledtext

win = tk.Tk()

win.title("Python GUI")

aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

def clickMe():
    action.configure(text='Hello ' + name.get())

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)
action.configure(state='disabled')

ttk.Label(win, text="Choose a Number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width = 12, textvariable = number)
numberChosen["values"] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1)
numberChosen.current(0)

chVardis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVardis, state='disabled')
check1.select()
check1.grid(column=0,row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2,row=4, sticky=tk.W)
def checkCallback():

    if chVarUn.get(): check3.configure(state='disabled')
    else:       check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:       check2.configure(state='normal')

chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())

scrolW = 50
scrolH = 3
scr = scrolledtext.ScrolledText(win, width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid(column=0, columnspan=3)

colors = ["Blue", "Gold", "Red"]

def radCall():
    radSel = radVar.get()
    if  radSel ==0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2:win.configure(background=colors[2])

radVar=tk.IntVar()

radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(win, text = colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)


nameEntered.focus()

win.mainloop()