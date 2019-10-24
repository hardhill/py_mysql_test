import mysql.connector

cnx = mysql.connector.connect(user='root', 
    password='t00r', 
    host='127.0.0.1', 
    database='infocenter3')
cursor=cnx.cursor()
cursor.execute("SELECT * FROM log")
result = cursor.fetchall()
for x in result:
    print(x[0],x[1])
cnx.close()