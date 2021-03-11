#smiley face
from tkinter import *
master=Tk()
canvas=Canvas(master,width=1000,height=1000,bg="black")
canvas.create_oval(200,200,800,800,fill="yellow")
canvas.create_oval(350,350,400,480,fill="black")
canvas.create_oval(600,350,650,480,fill="black")
canvas.create_arc(200,300+220,500,500-220,start=180,extent=180,style="arc")
canvas.pack()
mainloop()
