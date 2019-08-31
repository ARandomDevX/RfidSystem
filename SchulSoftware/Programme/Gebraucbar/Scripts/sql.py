from time import sleep
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import mysql.connector
from tkinter import messagebox
from tkinter import Listbox
import tkinter
from __variables__ import ortvar

ortvar = ortvar.get()


cur.execute('SELECT * FROM student')

sqlvar = cur.fetchall()


global run

run = 0

class Anmeldung:

    def anmelden(ort, status, zeit, incident, id):
        from Client import anmelden

        import datetime

        anmelden(ort=ort, zeit=zeit,status=status,incident = incident,id= id)

class Notfall:
    def Nifo(id):
        from Client import Notfall

        Notfall(id)

class delete:
    def delete(self, instance):
        from Client import Delete

        Delete(instance)
class sst:
        def sst(self, id):
            from Client import Status

            Status(id = id)




class nsa :
   def nsa(id,fname,lname,kl,erw1,erw2,add,n1,n2):

        import Client_NewUser

        Client.sendDataToServer(id = id ,fname = fname, lname = lname , kl = kl , erw1 =er1 , erw2 = erw2 , n1 =n1 , n2 = n2)


def informExit():

    ExitLog = open("ExitLog.txt","w")

    ExitLog.write("ExitLog.exit = /esbin.release.Sockets, Sockets.close==True.exit(), User.setStatement/Paremeter.exit(Var.www.html.xml.file, referToCmd.s)")