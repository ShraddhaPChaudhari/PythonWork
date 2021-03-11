#display report with item name,number and total price(total price=price*quantity)
import sqlite3
conn=sqlite3.connect('test1.db')
print('opened database sucessfully')
cursor=conn.execute('SELECT * FROM SHOP;')
for i in cursor:
    print('ITEMNO=',i[0])
    print('INAME=',i[1])
    print('total price=',i[2]*i[3])
conn.commit()
conn.close()

