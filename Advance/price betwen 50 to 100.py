#item name whose price in between 50 to 100
import sqlite3
conn=sqlite3.connect('test1.db')
print('opened database sucessfully')
cursor=conn.execute("SELECT * FROM SHOP WHERE (PRICE BETWEEN 50 AND 100);")
for i in cursor:
    print('ITEMNO=',i[0])
    print('INAME=',i[1])
    print('PRICE=',i[2])
    print('QUANTITY=',i[3])
print("done")
conn.commit()
conn.close()
