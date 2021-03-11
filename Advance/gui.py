from tkinter import *
def conversion():
    try:
        value=float(celcius.get())
        ferhnite.set((value*9/5+32))
    except ValueError:
        pass
def end():
    print("exit here")
root=Tk()
root.title("conversion")
celcius=StringVar()
ferhnite=StringVar()
a=Label(root,text="celcius").grid(row=0,column=1)
entry1=Entry(root,width=5,textvariable=celcius).grid(row=0,column=2)
b=Label(root,text="ferhnite").grid(row=1,column=1)
entry2=Label(root,width=5,textvariable=ferhnite).grid(row=1,column=2)
button=Button(text="calculate",command=conversion).grid(row=3,column=1)
button2=Button(text="exit",command=end).grid(row=4,column=1)

root.mainloop()

        
