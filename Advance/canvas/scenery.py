

from tkinter import *
master=Tk()
w=Canvas(master,width=600,height=500)
w.pack()
w.create_rectangle(0,0,600,100,fill="blue")
w.create_polygon(150,0,0,100,200,100,fill="brown")
w.create_polygon(200,100,300,0,400,100,fill="brown")
w.create_polygon(400,100,500,0,600,100,fill="brown")
w.create_oval(375,70,425,25,fill="yellow")
w.create_rectangle(0,100,600,500,fill="green")
w.create_rectangle(250,250,25,400,width=3,fill="yellow")
w.create_rectangle(200,300,125,400,width=3,fill="brown")
w.create_polygon(25,250,150,150,250,250,fill="red")
w.create_oval(40,300,95,360,fill="blue")
w.create_line(0,100,600,100,width=3)


