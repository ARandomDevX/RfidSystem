file = open('key.key', 'rb')
key = file.read()
file.close()
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt(pswdd,usddd):
    password_provided = pswdd # This is input in the form of a string
    password = password_provided.encode() # Convert to type bytes
    salt = os.urandom(16) # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
    from cryptography.fernet import Fernet
    message = password

    f = Fernet(key)
    encrypted = f.encrypt(message)
    from sql import cur
    cur.execute("SELECT * FROM rps WHERE passwd = {} ".format(encrypted))
    from sql import cur2
    cu2.execute('SELECT * FROM rps WHERE uname = {}'.format(usddd))
    res = 0
    if cur.rowcount >= 1 and cur2.rowcount >= 1:
        res = True
    elif cur.rowcount == 0 and cur2.rowcount == 0:
        res = False
    return res
def decrypt(pswdd,usdd):
    from cryptography.fernet import Fernet
    password_provided = pswdd  # This is input in the form of a string
    password = password_provided.encode()  # Convert to type bytes
    salt = os.urandom(16)  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    message = password

    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    return decrypted

