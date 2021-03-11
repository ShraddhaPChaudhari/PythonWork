#display all items information
import sqlite3
conn=sqlite3.connect('test1.db')
print('opened database sucessfully')
cursor=conn.execute('SELECT ITEMNO,INAME,PRICE,QUANTITY FROM SHOP;')
for row in cursor:
    print("ITEMNO=",row[0])
    print("INMAE=",row[1])
    print("PRICE=",row[2])
    print("QUANTITY=",row[3])
print('operation done')
conn.commit()
conn.close()

    
