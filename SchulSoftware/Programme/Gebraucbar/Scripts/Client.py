import socket

import atexit

import time

ip = open("ip.txt","r")

location = "hof"


sSock = socket(AF_INET, SOCK_STREAM)
sSock.connect((ip.read(), 1234))

def Raspberrypi():

	while True
		user = input()

		if user != "":

			sSock.sendall(user.encode("utf-8"))
			sSock.sendall("Type: Status".encode("utf-8"))

			data = sSock.recv(1079)

			while data.decode() != "Ready!":
				data =sSock.recv(1079)
			


			sSock.send(location.encode("utf-8"))

		else:
			pass

		if user == "exit":
			sSock.sendall(b"Command: Exit")
			sSock.close()

def Status(id,ort):
	from __variables__ import ortvar

	sSock.sendall(id.encode("utf-8"))

	sSock.sendall("Type: Status".encode("utf-8"))

	time.sleep(1)

	sSock.sendall(ortvar.get().encode("utf-8"))

def Notfall(person):

	sSock.sendall(f"{person}".encode("utf-8"))

	sScok.sendall("Type: Notfall")

def Anmelden(id,incident,zeit,ort,status):
	
	sSock.sendall(f"{id}".encode("utf-8"))

	sSock.sendall("Type: Anmelden/Abmelden".encode("utf-8"))

	time.sleep(1)

	sSock.sendall(incident.encode("utf-8"))

	sSock.sendall(zeit.encode("utf-8"))

	sSock.sendall(ort.encode("utf-8"))

	sSock.sendall(status.encode("utf-8"))

def Exit():

	sSock.close()

	exit()
def Delete(id):

	sSock.sendall(id.encode("utf-8"))

	sSock.sendall("Type: Delete")

while True:

	ExitLog = open("ExitLog.txt","r")

	if ExitLog.read() == "ExitLog.exit = /esbin.release.Sockets, Sockets.close==True.exit(), User.setStatement/Paremeter.exit(Var.www.html.xml.file, referToCmd.s)":

		from tkinter import messagebox

		asn  messagebox.askyesno("Wollen sie den Server Stoppen?")

		if asn == True:



			print("Server: Wird geschlossen")

			sSock.sendall("Type: Server.close().exitUsageFear=./False();")

		import time

		time.sleep(0.5)


		atexit.register(lambda : sSock.close())