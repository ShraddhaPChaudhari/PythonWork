
from tkinter import *             #import tkinter library
rangoli=Tk()                         #create a background window
rangoli.title('RANGOLI')              #window title 'RANGOLI'
canvas=Canvas(rangoli,height=550,width=550,bg='#CD5C5C')   

canvas.create_rectangle(50,50,500,500,fill='white',  #create square
                        outline="black",width=4)

#colour
canvas.create_polygon(50,250,50,150,150,150,fill="#00FFFF") #left top corner
canvas.create_polygon(150,50,150,150,250,50,fill="#00FFFF")
canvas.create_polygon(300,50,400,50,400,150,fill="#00FFFF") #right top corner
canvas.create_polygon(400,150,500,150,500,250,fill="#00FFFF")
canvas.create_polygon(50,300,150,400,50,400,fill="#00FFFF") #left bottom corner
canvas.create_polygon(150,400,150,500,250,500,fill="#00FFFF")
canvas.create_polygon(300,500,400,400,400,500,fill="#00FFFF") #right bottom corner
canvas.create_polygon(400,400,500,300,500,400,fill="#00FFFF")
canvas.create_polygon(260,260,200,200,250,150,250,50,300,50,
                      300,150,350,200,290,260,fill="#00FFFF")
canvas.create_polygon(260,260,200,200,150,250,50,250,50,300,
                      150,300,200,350,260,290,fill="#00FFFF")
canvas.create_polygon(260,290,200,350,250,400,250,500,300,500,
                      300,400,350,350,290,290,fill="#00FFFF")
canvas.create_polygon(290,290,350,350,400,300,500,300,500,250,
                      400,250,350,200,290,260,fill="#00FFFF")

canvas.create_rectangle(50,50,150,150,fill='yellow',    #create rectangle
                        outline="red",width=4)              #(in corners)
canvas.create_rectangle(400,50,500,150,fill='yellow',
                        outline="red",width=4)
canvas.create_rectangle(50,400,150,500,fill='yellow',
                        outline="red",width=4)
canvas.create_rectangle(400,400,500,500,fill='yellow',
                        outline="red",width=4)

canvas.create_polygon(50,250,150,250,250,150,250,50,width=4,  #create diyas base 
                      outline="blue",fill="#008080")
canvas.create_polygon(300,50,300,150,400,250,500,250,width=4,
                      outline="blue",fill="#800080")
canvas.create_polygon(50,300,150,300,250,400,250,500,width=4,
                      outline="blue",fill="#800080")
canvas.create_polygon(500,300,400,300,300,400,300,500,width=4,
                      outline="blue",fill="#008080")




canvas.create_line(200,200,260,260,fill="black",width=4)   
canvas.create_line(350,200,290,260,fill="black",width=4)
canvas.create_line(200,350,260,290,fill="black",width=4)
canvas.create_line(350,350,290,290,fill="black",width=4)

canvas.create_oval(250,250,300,300, outline="red",   #create circle
        fill="#00FF00", width=4)

canvas.pack()
