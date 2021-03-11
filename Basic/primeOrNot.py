#check wether a given number is prime or not?
for n in range(2,n+1):
    for x in range(2,n):
        if (n%x==0):
            print(n,'equals',x,'*',n//x)
            break
        else:
            print(n,'is a prime number')
