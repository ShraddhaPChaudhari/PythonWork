#display information whose name starts with 'P'
import sqlite3
conn=sqlite3.connect('test1.db')
print('opened database sucessfully')
cur=conn.execute('SELECT * FROM SHOP WHERE (INAME LIKE "P%");')
for i in cur:
    print('ITEMNO=',i[0])
    print('INAME=',i[1])
    print('PRICE=',i[2])
    print('QUANTITY=',i[3])
print("done")
conn.commit()
conn.close()


    
    

