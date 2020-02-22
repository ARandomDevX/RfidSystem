import requests
from flask import jsonify

# Config

lines = [line.rstrip('\n') for line in open('config.txt')]

Ip = lines[0]

Raspicode = lines[1]

# Send Data

Location = requests.get("http://" + Ip + "/assignLocation/" + Raspicode)

Location = Location.text

print(Location)

while True:

    Location = requests.get("http://" + Ip + "/assignLocation/" + Raspicode)

    CrdNumber = input()

    Out = requests.get("http://" + Ip + "/IsReg", data = {"Id" : CrdNumber})

    if "True" in Out:

        requests.post('http://' + Ip + '/rpisst', data = {'Id' : CrdNumber, 'Ort' : Location})


    elif "False" in Out:

        requests.post("http://" + Ip + "/RpiRegKid", data = {"Id" : CrdNumber})

        requests.post('http://' + Ip + '/rpisst', data={'Id': CrdNumber, 'Ort': Location})