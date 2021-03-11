#addition of two numbers till user wish
ans='y'
while(ans.casefold()=='y'):
    no1=int(input('enter 1st number'))
    no2=int(input('enter 2nd number'))
    addition=no1+no2
    print('sum of two numbers are',addition)
    ans=input('do you want to continue(y/n)?')
    
