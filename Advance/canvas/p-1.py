def call():
    fhand=open('demo.txt','w')
    fhand.write('Jack and jill\n Went up the hill\n To fetch the pail of water\n Jack fell down and broke his crown\n and jill came tumbling after')
    fhand.close()
call()
ghand=open('demo.txt','r')
print(ghand.readline())
print(ghand.read())

hand=open('demo.txt','r')
print(hand.append(input('enter the text as your wish')))
print(hand.read())
