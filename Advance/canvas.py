# canvas assignment
# railway engine
from tkinter import *
master=Tk()
w=Canvas(master,width=200,height=100)
w.pack()
w.create_rectangle(34,20,68,40,fill="black")
w.create_rectangle(50,20,150,80,fill="brown")
w.create_rectangle(34,10,68,20,fill="black")
w.create_oval(50,50,100,100)
w.create_oval(100,100,200,200)
