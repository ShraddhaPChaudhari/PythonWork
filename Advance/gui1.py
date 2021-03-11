#celcius to farnehnite
from tkinter import *
def calculate(*args):
    try:
        value=float(celsius.get())
        farnehnite.set((value*9/5+32))
    except ValueError:
        pass
root=Tk()
root.title("celsius to farnehnite")
mainframe=Frame(root)
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)
celsius=StringVar()
farnehnite=StringVar()
celsius_entry=Entry(mainframe,width=7,textvariable=celsius)
celsius_entry.grid(column=2,row=1,sticky=(W,E))
a=Entry(mainframe,textvariable=farnehnite).grid(column=2,row=2,sticky=(W,E))
b=Button(mainframe,text="Calculate",command=calculate).grid(column=3,row=3,sticky=W)
c=Label(mainframe,text="celsius").grid(column=3,row=1,sticky=W)
d=Label(mainframe,text="is eqivalent to").grid(column=1,row=2,sticky=E)
e=Label(mainframe,text="farnehnite").grid(column=3,row=2,sticky=W)
celsius_entry.focus()
root.bind("<Return>",calculate)
root.mainloop()
