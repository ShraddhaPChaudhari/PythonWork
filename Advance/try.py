from tkinter import *
def add():
    val1=int(num1.get())
    val2=int(num2.get())
    result.set(val1+val2)
def prod():
    val1=int(num1.get())
    val2=int(num2.get())
    result.set(val1*val2)
root=Tk()
root.title("Addition and product")
num1=IntVar()
num2=IntVar()
result=IntVar()
var=IntVar()
l=Label(root,text="enter first number:").grid(row=1,column=0)
num1_entry=Entry(root,width=6,textvariable=num1).grid(row=1,column=1)
l2=Label(root,text="enter second number:").grid(row=2,column=0)
num2_entry=Entry(root,width=6,textvariable=num2).grid(row=2,column=1)
sum_button=Radiobutton(root,text="sum",command=add,variable=var,value=1).grid(row=3,column=0)
prod_button=Radiobutton(root,text="product",command=prod,variable=var,value=2).grid(row=3,column=1)
l3=Label(text="result").grid(row=5,column=1)
Label(root,textvariable=result).grid(row=5,column=2)
exit=Button(root,text="exit",command=root.destroy)
root.mainloop()


