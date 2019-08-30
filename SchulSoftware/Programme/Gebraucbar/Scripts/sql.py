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




cur.execute('SELECT * FROM student')

sqlvar = cur.fetchall()


global run

run = 0

class Anmeldung:

    def anmelden(ort, status, zeit, incident, id):
        try:
            

            import datetime

            print(id)
            cur.execute('INSERT INTO angemeldet VALUES({},{})'.format(id.get(), status))
            cur.execute('''INSERT INTO meldung VALUES ({},{},{},{})

                ON DUPLICATE KEY UPDATE ort = {}, zeit = {}, id = {}, incident = {}'''.format(ort, zeit , id ,incident,ort, zeit , id ,incident))
        except FileExistsError as er:
            messagebox.showerror('Fehler','{} ein Fehler ist aufgetreten, bitte versuchen es sie nochmals oder infromieren es!'.format(lambda : datetime.datetime.now()))


class Notfall:
    def Nifo(id):
        import Client

        Notfall(id)

class delete:
    def delete(self, instance):
        cur.execute('DELETE * FROM student WHERE id={}'.format(instance))
        cur.execute()
        mydb.commit()
class sst:
        def sst(self, id):
            import datetime
            try:
                from time import sleep

                cur.execute('SELECT * FROM student WHERE id = {}'.format(id))

                records = cur.fetchall()
                num = 0
                if cur.rowcount == 0:
                    messagebox.showerror('Fehler','Prozes kann nicht weiter geführt werden,Peron ist nicht in der datenbank eingetragen')
                    from time import sleep
                    sleep(1)
                    messagebox.showinfo('Info','Sie können die person in die datenbank eintragen an dem sie die seite aufüllen um eine Person anzumelden')



                else:

                    cur.execute("""
                                                                                   INSERT INTO status VALUES('{}','{}')
                                                                                   ON DUPLICATE KEY UPDATE id = '{}', status = '{}';
                    
                                                                   """.format(id, ortvar.get(), id, ortvar.get()))

                    sleep(1)
                    messagebox.showinfo('Erfolgreich',
                                                    'Staus von {}, wurde verändert {}'.format(id, datetime.datetime.now(),datetime.datetime.now()))
                    mydb.commit()
            except:

                from time import sleep
                sleep(1)
                messagebox.showerror('Fehler','Ein Fehler ist aufgetreten.Der Rechner guckt was es war')

                if id == "":
                    messagebox.showinfo('Gefunden','Drücken sie auf das feld und danach scannen.')
                elif id.isdigit() == False :
                    messagebox.showinfo('Gefunden','Bitte scannen sie die karte weil hier sind buchstaben.')

                else:
                    messagebox.showerror('Nicht Gefunden','Entschuldigung, dieser fehler ist nicht in der Fehler tabele,fehlersuchversuch 2 beginnt')
                    import datetime
                    try:
                        from time import sleep


                        cur.execute("""
                                                                                           INSERT INTO status VALUES('{}','{}')
                                                                                           ON DUPLICATE KEY UPDATE id = '{}', status = '{}';

                                                                           """.format(id, ortvar.get(),id,ortvar.get()))

                        sleep(1)
                        messagebox.showinfo('Erfolgreich',
                                            'Staus von {}, wurde verändert {}'.format(id, datetime.datetime.now(), id,
                                                                                      datetime.datetime.now()))
                        mydb.commit()
                    except EOFError as e:
                        messagebox.showinfo('Fehler','Der Fehler wurde gefunden:{}'.format(e))


class nsa :
    def nsa(self,id,fname,lname,klasse,erw1,erw2,add,n1,n2):
        cur.execute('INSERT INTO student VALUES({},{},{},{})').fromat(id,fname,lname,klasse)
        cur.execute('INSERT INTO notfall VALUES({},{},{},{},{},{},{})').format(id,erw1,erw2,add,n1,n2,klasse)
