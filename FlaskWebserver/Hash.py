import bcrypt



def hashPassword(password):

    Salt = b'$2b$12$hFo/Hp4u4NuOWXHlONDAJO'


    return bcrypt.hashpw(password=password.encode('utf-8'), salt=Salt)