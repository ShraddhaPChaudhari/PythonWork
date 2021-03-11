#exception handling
def division(num,den):
    try:
        div=(num/den)
    except ZeroDivisionError:
        print("pls enter valid denominator")
    else:
        print("the division is:",div)
num=int(input("enter the numerator:"))
den=int(input("enter the denominator:"))
division(num,den)
