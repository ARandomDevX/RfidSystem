from cryptography.fernet import Fernet

def Encrypt(String):

	File = open("KeyValues1.sha.key","r")

	Key = File.read()

	Generator = Fernet(Key)

	EncryptedString = Generator.encrypt(String)

	return EncryptedString

	File.close()

def Decrypt(String):

	File = open("KeyValues1.sha.key","r")

	Key = File.read()

	Generator = Fernet(Key)

	DecryptedString = Generator.decrypt(String)

	return DecryptedString

	File.close()

def GenerateKey():

	Key = Fernet.generate_key()

	File = open("KeyValues1.sha.key", "w")

	File.write(Key)

	File.close()