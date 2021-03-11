from tkinter import *
root=Tk()
l=Canvas(root,width=1000,height=1000)
l.pack()
l.create_rectangle(680,10,690,25,fill="red")

l.create_oval(80,80,125,125,fill="black")
l.create_oval(175,80,220,125,fill="black")

l.create_rectangle(50,25,250,100,fill="blue")

l.create_rectangle(60,35,90,50,fill="yellow")
l.create_rectangle(100,35,130,50,fill="yellow")
l.create_rectangle(140,35,170,50,fill="yellow")
l.create_rectangle(180,35,210,50,fill="yellow")
l.create_rectangle(220,35,245,50,fill="yellow")

l.create_rectangle(250,55,275,65,fill="red")

l.create_oval(305,80,350,125,fill="black")
l.create_oval(400,80,445,125,fill="black")

l.create_rectangle(275,25,475,100,fill="blue")

l.create_rectangle(285,35,315,50,fill="yellow")
l.create_rectangle(325,35,355,50,fill="yellow")
l.create_rectangle(365,35,395,50,fill="yellow")
l.create_rectangle(405,35,435,50,fill="yellow")
l.create_rectangle(445,35,470,50,fill="yellow")

l.create_rectangle(475,55,500,65,fill="red")

l.create_oval(530,80,575,125,fill="black")
l.create_oval(625,80,670,125,fill="black")

l.create_rectangle(500,25,700,100,fill="blue")

l.create_rectangle(510,35,540,50,fill="yellow")
l.create_rectangle(550,35,580,50,fill="yellow")
l.create_rectangle(590,35,620,50,fill="yellow")
l.create_rectangle(630,35,695,50,fill="yellow")


mainloop()
