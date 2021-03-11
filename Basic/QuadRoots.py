#program to compute the real roots of the quadratic equation ax^2+bx+c=0
a=float(input('enter the value for the coefficient of x^2.'))
b=float(input('enter the value for the coefficient of x.'))
c=float(input('enter the value of the constant term. '))
d=(b**2)-(4*a*c)
x1 = (-b+(d**(1/2)))/2*a
x2 = (-b+(d**(1/2)))/2*a
if a==0 and b==0:
    print('the equation has no roots')
elif a==0:
    x=(-b+sqrt(d))/(2*a)
    print('the quation has only one root and it is',-c/b)
elif d<0:
    print('the roots are not real')
else:
    print('the roots are: ',x1, 'and', x2)
