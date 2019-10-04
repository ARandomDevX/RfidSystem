import mysql.connector

import bcrypt

mydb = mysql.connector.connect(
    host='localhost',
    database ="dev",
    user='developer',
    passwd='DevAnantha',
    auth_plugin='mysql_native_password'
)

global cur

cur = mydb.cursor()

def getSalt():



    cur.execute('SELECT * FROM salt')

    preSalt = cur.fetchall()

    print(preSalt[0])
    
    #salt = bytearray(str(preSalt))

    #return salt

print(getSalt())
