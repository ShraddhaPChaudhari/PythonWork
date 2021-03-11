#age
def GetAge():
    try:
        age=int(input("enter the age of the user:"))
    except ValueError:
        print("pls enter correct age")
    else:
        print("your age is:",age)
GetAge()
