import socket
import threading


# Creating the required Objs

run = 0


S =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mydb = mysql.connector.connect(
    host='192.168.0.31',
    database ="school",
    user='user',
    passwd='1234',
    auth_plugin='mysql_native_password'
)

cur = mydb.cursor()

# Data handler(Stage 2)

S.bind(("0.0.0.0", 1234))

class Notfall:
    def Nifo(self,id):
        from time import sleep
        try:

            root = tkinter.Tk()
            cur.execute('SELECT * FROM student WHERE id = {}'.format(id))

            records = cur.fetchall()
            num = 0
            if cur.rowcount == 0:
                messagebox.showerror('Fehler',
                                     'Prozes kann nicht weiter geführt werden,Person ist nicht in der datenbank eingetragen')
                from time import sleep
                sleep(1)
                messagebox.showinfo('Info','Sie können die person in die datenbank eintragen an dem sie die seite aufüllen um eine Person anzumelden')
            else:
                messagebox.showinfo('Prozess startet....')
                sleep(1)
                cur.execute('SELECT * FROM notfall WHERE id ={}'.format(id))
                exe = cur.fetchall()
                return exe
        except:
            if id == '' and run ==1 or id == '' and run == 0:
                pass
            if id =='' and run != 1 or id == '' and run != 0:
                messagebox.showerror('Fehler','Bitte drücken sie auf dass feld un scannen danach')


def HandleNotfall(data):

	cur.execute(f"SELECT * FROM notfall WHERE id = {data}")

	return cur.fetchall()
def HandleNewMember(id,fname,lname,kl):

	cur.execut(f"INSERT INTO studet VALUES({id},{fname},{lname},{kl})")


# Data handler(Stage 1)
def Handler(c,a):
	while True:
		data2 = c.recv(1078).decode("utf-8")
		data = c.recv(1079).decode("utf-8")

		if run !=0:
			if data == "Type: Status":
				c.sendall("Ready!".encode("utf-8"))
				data = c.recv(1079).decode("utf-8")
				sst.sst(id = data2)
			elif data == "Type: Notfall":
				c.send(Notfall.Nifo(id = data))
			elif data == "Type: Add new member":
				c.sendall("Ready!".encode("utf-8"))
				data3 = c.recv(1078)
			elif data == "Command: Exit":
				c.sendall("Closing".encode("utf-8"))
				S.close()
			elif data == "Type: Anmelden/Abmelden":
				Anmelden.anmelden(id = data)

			run = 0
		 	
		else:
			pass

		if not data:
			break;

# sst
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


# Doing action
while True:

	c, a = S.accept()

	cThread = threading.Thread(target=handler,args=(c,a))

	cThread.deamon = True

	cThread.start()




