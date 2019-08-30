import socket

ip = open("ip.txt","r")

location = "hof"


sSock = socket(AF_INET, SOCK_STREAM)
sSock.connect((ip.read(), 1234))

def Status():

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

def Notfall(person):

	sSock.sendall(f"{person}".encode("utf-8"))

	sScok.sendall("Type: Notfall")