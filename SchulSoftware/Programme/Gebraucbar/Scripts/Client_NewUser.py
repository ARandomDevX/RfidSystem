import socket

import time



ip = open("ip.txt","r")



sSock = socket(AF_INET, SOCK_STREAM)
sSock.connect((ip.read(), 1234))
class Client:

	def sendDataToServer(id,fname,lname,kl,erw1,erw2,n1,n2):

		# Send The Identity

		sSock.sendall(f"{id}".encode("utf-8"))

		# Send The Usage

		sSock.sendall("Type: Add new member"encode("utf-8"))

		# Give the server time

		time.sleep(0.5)

		# Send The parameters

		sSock.sendall(fname.encode("utf-8"))

		sSock.sendall(lname.encode("utf-8"))

		sSock.sendall(kl.encode("utf-8"))

		sSock.sendall(erw1.encode("utf-8"))

		sSock.sendall(erw2.endcode("utf-8"))

		sSock.sendall(n1.encode("utf-8"))

		sSock.sendall(n2.encode("utf-8"))
