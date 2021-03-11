#program to process eligible candidate for admission to engineering course
m=int(input('enter the marks in maths'))
p=int(input('enter the marks in physics'))
c=int(input('enter the marks in chemistry'))
t1=m+p+c
t2=p+m
if (m>60 and p>=50 and c>=40):
    if (t1>=200 or t2>=150):
        print('you arr eligible candidate for engineering')
    else:
        print('you are not eligible for engineering. sorry!')
else:
    print('you are not eligible')
