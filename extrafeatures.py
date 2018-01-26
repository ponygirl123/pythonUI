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

nameEntered.focus()

win.mainloop()