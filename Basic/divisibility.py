#to check whether entered number is divisible by 3 or 7 or both
a=int(input('enter the number'))
if(a%3==0 and a%7==0):
    print('the number is divisible by both 3 and 7')
elif(a%3==0):
    print('the number is divisible by 3')
else:
    print('the number is divisible by 7')
