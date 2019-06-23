import mysql.connector
import datetime
mydb = mysql.connector.connect(
            host = 'localhost',
            database = 'school',
            user = 'root',
            passwd = 'ananthiscool',
            auth_plugin='mysql_native_password'
        )
cur = mydb.cursor()

while 1!=2:
    idint = input('id')
    time = datetime.datetime.now()
    cur.execute('INSERT INTO school.meldung(ort,zeit,id) VALUES ("hof","{}","{}")'.format(time,idint))
    mydb.commit()

