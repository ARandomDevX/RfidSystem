import socket



ip = open("ip.txt","r")



sSock = socket(AF_INET, SOCK_STREAM)
sSock.connect((ip.read(), 1234))
class Client:

	def sendDataToServer(id,fname,lname,kl):

		# Send The Identity

		sSock.sendall(f"{id}".encode("utf-8"))

		# Send The Usage

		sSock.sendall("Type: Add new member"encode("utf-8"))

		# Send The parameters

		sSock.sendall(fname.encode("utf-8"))

		sSock.sendall(lname.encode("utf-8"))

		sSock.sendall(kl.encode("utf-8"))





