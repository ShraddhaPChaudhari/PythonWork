#floatinng pt
def GetInt():
    try:
        a=int(input("enter an integer:"))
    except ValueError:
        print("enter a valid number")
    else:
        print("the entered number is:",a)
GetInt()
