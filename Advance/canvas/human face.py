#program to draw human face
from tkinter import *
face=Tk()
face.title("human face")
canvas=Canvas(face,height=600,width=600,bg="white")
canvas.create_oval(130,130,430,430,fill="pink",outline="black",width=2)
canvas.create_rectangle(130,200,420,200,fill="black",outline="black",width=3)
canvas.create_oval(200,250,250,300,fill="pink",outline="black",width=2)
canvas.create_oval(300,250,350,300,fill="pink",outline="black",width=2)
canvas.create_line(250,340,280,350,300,340,fill="black",width=3)
canvas.create_arc(240,360,320,400,start=180,extent=175,fill="red",width=2)
canvas.pack()
