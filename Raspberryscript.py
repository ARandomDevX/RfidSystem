import request

url = '192.168.0.31/rpisst'


while True:

    Id = input()

    Ort = 'Hof'

    Body = {Id:Ort}

    request.post(url,data=Body)
