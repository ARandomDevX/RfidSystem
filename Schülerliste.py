

from tkinter import ttk
from tkinter import Tk
from tkinter import _tkerror
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    database='school',
    user='root',
    passwd='ananthiscool',
    auth_plugin='mysql_native_password'
    )
mydb1 = mysql.connector.connect(
    host='localhost',
    database='school',
    user='root',
    passwd='ananthiscool',
    auth_plugin='mysql_native_password'
    )
mydb2 = mysql.connector.connect(
    host='localhost',
    database='school',
    user='root',
    passwd='ananthiscool',
    auth_plugin='mysql_native_password'
    )



cur = mydb.cursor()
cur2 = mydb1.cursor()
cur3 = mydb2.cursor()
mydb3 = mysql.connector.connect(
    host='localhost',
    database='school',
    user='root',
    passwd='ananthiscool',
    auth_plugin='mysql_native_password'
    )
cur4 = mydb3.cursor()
mydb4 = mysql.connector.connect(
    host='localhost',
    database='school',
    user='root',
    passwd='ananthiscool',
    auth_plugin='mysql_native_password'
    )

cur5 = mydb4.cursor()
root = Tk()
cur2.execute('SELECT fname FROM student')
cur3.execute('SELECT lname FROM student')

cur2.fetchall()
cur3.fetchall()
tree = ttk.Treeview(root)
tree.pack()

tree.insert('','0','i1',text='Waldschule')
inum = 0
pos = 0
cur.execute('')
for item2 in cur2.fetchall():
    for item in cur2.fetchone():
        inum+=1
        pos+=1
        tree.insert('i1','i{}','{}',text='{}'.format(inum,pos,cur2 + ' ' + cur3))

root.mainloop()
