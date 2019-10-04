import requests


statusPayloadPart = open('Status.txt','r')

statusPayloadPart = statusPayloadPart.read()

while True:

    lineList = [line.rstrip('\n') for line in open('ip.txt')]

    lineList = list(lineList)

    Rfid_Card_Number = input()

    if Rfid_Card_Number != '' :

        try:
            from collections import OrderedDict

            data_pice1 = Rfid_Card_Number

            data_pice2 = statusPayloadPart

            data_pice3 = 'rfid.number'

            data_pice4 = 'status'

            data = {data_pice3:data_pice1,data_pice4:data_pice2}

                
            url = str('http://' + lineList[0] + '/Data')


            requests.post(url = url, data=data)
        except:
            pass


    else:
        pass