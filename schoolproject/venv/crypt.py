file = open('key.key', 'rb')
key = file.read()
file.close()
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt(pswdd,usddd):
    hashlib.sha224(b"{}").hexdigest().format(pswdd)
    from sql import cur
    cur.execute("SELECT * FROM rsb WHERE pass = {}".format(pswdd))
    res = 0
    if cur.rowcount() == 0:
        res = False
    elif cur.rowcount() > 1:
        res = True
def enrypt_for_insert(pswdd,usdd):
    hash = hashlib.sha224(b"{}").hexdigest().format(pswdd)
    return hash
