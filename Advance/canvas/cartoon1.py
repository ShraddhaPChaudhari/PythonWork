#cartoon1
from tkinter import *
master=Tk()
w=Canvas(master,width=350,height=350)
w.pack()
w.create_oval(50,100,310,280,fill="yellow")
w.create_oval(100,150,150,180,fill="red")
w.create_oval(200,150,250,180,fill="red")
w.create_line(100,210,260,210,fill="red")
