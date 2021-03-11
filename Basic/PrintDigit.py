#program to print digits of a number
no=int(input('enter any number'))
while(no!=0):
    rem=no%10
    print(' ',rem)
    no=no//10
