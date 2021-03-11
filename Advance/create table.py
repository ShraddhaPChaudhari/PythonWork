#database in python
import sqlite3
conn=sqlite3.connect('test1.db')
print('database opened sucessfully')
conn.execute('CREATE TABLE SHOP\
(ITEMNO INT PRIMARY KEY NOT NULL,\
INAME TEXT NOT NULL,\
PRICE INT NOT NULL,\
QUANTITY REAL);')
print("table created sucessfully")
conn.execute("INSERT INTO SHOP(ITEMNO,INAME,PRICE,QUANTITY)\
VALUES(101,'GEOMETRY BOX',50,100)");
conn.execute("INSERT INTO SHOP(ITEMNO,INAME,PRICE,QUANTITY)\
VALUES(102,'SOAP',100,50)");
conn.execute("INSERT INTO SHOP(ITEMNO,INAME,PRICE,QUANTITY)\
VALUES(103,'PERFUME',150,25)");
conn.execute("INSERT INTO SHOP(ITEMNO,INAME,PRICE,QUANTITY)\
VALUES(104,'PEN',50,200)");
conn.execute("INSERT INTO SHOP(ITEMNO,INAME,PRICE,QUANTITY)\
VALUES(105,'PENCIL',20,100)");
conn.commit()
print("records inserted sucessfullly")
conn.close()
