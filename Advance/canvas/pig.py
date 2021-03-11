from tkinter import *
root=Tk()
l=Canvas(root,width=1000,height=1000)
l.create_oval(150,60,250,150,fill="green")
l.create_oval(300,20,400,120,fill="green")
l.create_oval(180,90,240,140,fill="black")
l.create_oval(330,50,390,110,fill="black")
l.create_oval(100,100,600,600,fill="green")
l.create_oval(150,300,250,400,fill="white")
l.create_oval(425,300,525,400,fill="white")
l.create_oval(170,330,200,360,fill="black")
l.create_oval(475,330,505,360,fill="black")
l.create_oval(260,390,425,515,fill="grey")
l.create_oval(250,350,430,480,fill="#476042")
l.create_oval(290,400,330,435,fill="black")
l.create_oval(355,400,395,435,fill="black")



l.pack()
mainloop()
