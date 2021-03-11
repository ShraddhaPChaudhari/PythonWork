#display soap info
import sqlite3
conn=sqlite3.connect('test1.db')
print('opened database sucessfully')
cur=conn.execute('SELECT * from SHOP where INAME="SOAP";')
for i in cur:
    print('ITEMNO=',i[0])
    print('INAME=',i[1])
    print('PRICE=',i[2])
    print('QUANTITY=',i[3])
print("done")
conn.commit()
conn.close()

