def encrypt(sentence):

    result = []

    for letter in sentence:

        l = ord(letter) - 20

        result.append(l)

    for numbers in result:

        print(numbers, end="")

        print("",end="")

    return str()


def decrypt(sentence):

    pass

print(encrypt("Hello"))
