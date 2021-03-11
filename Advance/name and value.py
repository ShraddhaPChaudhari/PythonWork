#display item name and price
import sqlite3
conn=sqlite3.connect('test1.db')
curr=conn.execute("SELECT ITEMNO,INAME,PRICE,QUANTITY from SHOP")
for row in curr:
    print("INAME=",row[0])
    print("PRICE=",row[1],"\n")
print("Operation done successfully")
conn.commit()
conn.close()
