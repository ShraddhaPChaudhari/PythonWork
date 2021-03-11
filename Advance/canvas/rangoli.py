from tkinter import *

master = Tk()

w = Canvas(master, width=600, height=600)
w.pack()

w.create_rectangle(0, 0, 600, 600,fill="pink")
w.create_line(50, 0, 50, 50,fill="maroon",width=3)
w.create_line(0, 50, 50, 50,fill="maroon",width=3)
w.create_line(0, 50, 50, 100,fill="maroon",width=3)
w.create_line(50,100, 50,150,fill="maroon",width=3)
w.create_line(50,150,0,200,fill="maroon",width=3)
w.create_line(0,200,50,200,fill="maroon",width=3)
w.create_line(50, 200, 50, 400,fill="maroon",width=3)
w.create_line(0, 400, 50, 400,fill="maroon",width=3)
w.create_line(0, 400, 50, 450,fill="maroon",width=3)
w.create_line(50,450, 50,500,fill="maroon",width=3)
w.create_line(0,500,0,500,fill="maroon",width=3)
w.create_line(50,500,0,550,fill="maroon",width=3)
w.create_line(0, 550, 50, 550,fill="maroon",width=3)
w.create_line(50,550, 50, 600,fill="maroon",width=3)
w.create_line(50, 600, 100, 550,fill="maroon",width=3)
w.create_line(100,550, 150,550,fill="maroon",width=3)
w.create_line(150,550,200,600,fill="maroon",width=3)
w.create_line(200,600,200,550,fill="maroon",width=3)
w.create_line(200, 550, 400, 550,fill="maroon",width=3)
w.create_line(400, 550, 400, 600,fill="maroon",width=3)
w.create_line(400, 600, 450, 550,fill="maroon",width=3)
w.create_line(450, 550, 500, 550,fill="maroon",width=3)
w.create_line(500, 550, 550, 600,fill="maroon",width=3)
w.create_line(550,600, 550,550,fill="maroon",width=3)
w.create_line(550,550,600,550,fill="maroon",width=3)
w.create_line(600,550,550,500,fill="maroon",width=3)
w.create_line(550, 500, 550, 450,fill="maroon",width=3)
w.create_line(550, 450, 600, 400,fill="maroon",width=3)
w.create_line(600, 400, 550, 400,fill="maroon",width=3)
w.create_line(550, 400, 550, 200,fill="maroon",width=3)
w.create_line(550, 200, 600, 200,fill="maroon",width=3)
w.create_line(600,200, 550,150,fill="maroon",width=3)
w.create_line(550,150,550,100,fill="maroon",width=3)
w.create_line(550,100,600,50,fill="maroon",width=3)
w.create_line(600, 50, 550, 50,fill="maroon",width=3)
w.create_line(550, 50, 550, 0,fill="maroon",width=3)
w.create_line(550, 0, 500, 50,fill="maroon",width=3)
w.create_line(500, 50, 450, 50,fill="maroon",width=3)
w.create_line(450, 50, 400, 0,fill="maroon",width=3)
w.create_line(400,0, 400,50,fill="maroon",width=3)
w.create_line(400,50,200,50,fill="maroon",width=3)
w.create_line(200,50,200,0,fill="maroon",width=3)
w.create_line(200, 0, 150, 50,fill="maroon",width=3)
w.create_line(150, 50, 100, 50,fill="maroon",width=3)
w.create_line(100, 50, 50, 0,fill="maroon",width=3)

w.create_rectangle(200, 200, 400, 400,fill="green")
w.create_rectangle(100, 100, 150, 150,fill="blue")
w.create_rectangle(450, 450, 500, 500,fill="blue")
w.create_rectangle(450, 100, 500, 150,fill="blue")
w.create_rectangle(100, 450, 150, 500,fill="blue")
point1 = [300, 50, 350, 100, 350, 150, 300, 
    200, 250, 150, 250, 100]

point2 = [100, 250, 150, 250, 200, 300, 150, 
    350, 100, 350, 50, 300]

point3 = [450, 250, 500, 250, 550, 300, 500, 
    350, 450, 350, 400, 300]

point4 = [300, 400, 350, 450, 350, 500, 300, 
    550, 250, 500, 250, 450]

w.create_polygon(point2, outline='red', 
    fill='yellow', width=2)
w.create_polygon(point3, outline='red', 
    fill='yellow', width=2)
w.create_polygon(point1, outline='red', 
    fill='yellow', width=2)
w.create_polygon(point4, outline='red', 
    fill='yellow', width=2)
mainloop()
