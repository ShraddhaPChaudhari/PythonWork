#factorial of a number given by user
fact=1
no=int(input('enter any number'))
while(no!=0):
    fact=fact*no
    no=no-1
print('factorial of a number is',fact)
