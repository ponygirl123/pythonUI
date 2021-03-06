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

COLOR1 = "Blue"
COLOR2 = "Green"
COLOR3 = "Red"

def radCall():
    radSel = radVar.get()
    if  radSel ==1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3:win.configure(background=COLOR3)

radVar=tk.IntVar()

rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

nameEntered.focus()

win.mainloop()