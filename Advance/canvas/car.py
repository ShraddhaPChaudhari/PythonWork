
from tkinter import *             #import tkinter library
car=Tk()                         #create a background window
car.title('car')              #window title 'car'
canvas=Canvas(car,height=600,width=600,bg="white")

canvas.create_polygon(150,300,20,300,20,400,580,400,
                      580,300,500,300,fill="red",
                      outline="black",width=3)
canvas.create_polygon(200,200,100,300,500,300,400,200,
                      fill="black",width=3)
canvas.create_line(300,200,300,400,fill="yellow",width=3)
canvas.create_line(250,320,280,320,fill="yellow",width=3)
canvas.create_line(450,320,480,320,fill="yellow",width=3)

#headlight
canvas.create_rectangle(20,330,40,380,fill="yellow",width=3)
canvas.create_rectangle(550,320,580,340,fill="yellow",width=3)
canvas.create_rectangle(550,350,580,380,fill="yellow",width=3)

#wheel
canvas.create_oval(150,380,250,450,fill="black",width=3)
canvas.create_oval(400,380,500,450,fill="black",width=3)


canvas.pack()
