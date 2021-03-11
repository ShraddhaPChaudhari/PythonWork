#to interchange the values of two variable with and without using temp. variable
a=int(input('enter the first number'))
b=int(input('enter the second number'))
print('value of a=',a,' ','value of b=',b)
temp=0
temp=a
a=b
b=temp
print('the interchanged values using temp variable are-\nvalue of a=',a,'\nvalue of b=',b)

a=int(input('\nenter the first number'))
b=int(input('enter the second number'))
print('value of a=',a,' ','value of b=',b)
(a,b)=(b,a)
print('the interchanged values without using temp variable are-\nvalue of a=',a,'\nvalue of b=',b)
