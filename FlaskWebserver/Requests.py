import requests
import os

def delete(id):

    lineList = [line.rstrip('\n') for line in open('ip.txt')]

    lineList = list(lineList)

    Rfid_Card_Number = id

    if id != '' :
        
        try:
            
            data_pice1 = Rfid_Card_Number

            data_pice3 = 'rfid.number'
        
            url = str('http://' + lineList[0] + '/del' + '/' + Rfid_Card_Number)

            requests.delete(url = url)
        except:
            pass


    else:
        pass

def sst(id):

    import requests


    statusPayloadPart = open('Status.txt','r')

    statusPayloadPart = statusPayloadPart.read()


    lineList = [line.rstrip('\n') for line in open('ip.txt')]

    lineList = list(lineList)

    Rfid_Card_Number = id

    if Rfid_Card_Number != '' :

        try:
            from collections import OrderedDict

            data_pice1 = Rfid_Card_Number

            data_pice2 = statusPayloadPart

            data_pice3 = 'rfid.number'

            data_pice4 = 'ja'

            data = {data_pice3:data_pice1,data_pice4:data_pice2}

                    
            url = str('http://' + lineList[0] + '/sst')


            requests.post(url = url, data=data)
        except:
            pass


        else:
            pass

def nsa():

    lineList = [line.rstrip('\n') for line in open('ip.txt')]

    url = 'http://' + lineList[0] + '/nsa/<string:id>/<string:fname>/<string:lname>/<string:kl>/<string:erw1>/<string:erw2>/<string:n1>/<string:n2>'
    
    requests.post(url=url)
def closeServer(reboot=False):

    import atexit

    import os

    import requests

    lineList = [line.rstrip('\n') for line in open('ip.txt')]

    if reboot != False:

        url = 'http://' + lineList[0] + '/closeServer'

        requests.post(url=url)
    else:

        url = 'http://' + lineList[0] + '/closeServer'

        requests.post(url=url)


def notfall(id):
    
    lineList = [line.rstrip('\n') for line in open('ip.txt')]

    url = 'http://' + lineList[0] + '/notfall'

    payload = {'id':id}

    GetRequest = requests.get(url=url,data=payload)

    return GetRequest

print(notfall(id='5678').json())
