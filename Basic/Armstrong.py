#program to accept number from user and check whether itis armstrong or not
no=int(input('enter the number to check whether it is armstrong or not: '))
s=0
temp=no
while(no!=0):
    r=no%10
    b=r*r*r
    s=s+b
    no=no//10
    c=s
if(c==temp):
    print('it is armstrong number')
else:
    print('it is not armstrong number')
