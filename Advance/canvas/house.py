#program to draw house
from tkinter import *
master=Tk()
canvas=Canvas(master,height=600,width=600,bg="white")
canvas.create_polygon(80,480,250,480,250,580,80,580,80,480,50,450,30,480,30,580,80,580,fill="pink",outline="black",width=3)
canvas.pack()
canvas.create_polygon(50,450,80,480,250,480,200,450,fill="brown",outline="black",width=3)
canvas.create_polygon(100,530,100,580,150,580,150,530,fill="yellow",outline="black",width=3)
canvas.create_rectangle(180,520,230,550,fill="blue",outline="black",width=3)
