def Encrypt():
    from cryptography.fernet import Fernet
    try:
        with open('key.key','rb') as file1:
            file1.read()
        key = file1.encode('utf-8')
    except:
        from cryptography.fernet import Fernet
        key = Fernet.generate_key()

        with open('key.key','wb') as file1:

            file1.write(key)

    input_file = 'test.txt'
    output_file = 'out.en'

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)
    return encrypted

def Decrypt():
    from cryptography.fernet import Fernet

    try:
        with open('key.key','rb') as file1:
            file1.read()
        key = file1.encode('utf-8')
    except:
        from cryptography.fernet import Fernet
        key = Fernet.generate_key()

        with open('key.key','wb') as file1:

            file1.write(key)

    input_file = 'test.txt'
    output_file = 'out.txt'

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)
    return encrypted


with open('test.txt','w') as file:

    file.write('Tak')

print(Encrypt())

print(Decrypt())