import requests


# Config

lines = [line.rstrip('\n') for line in open('config.txt')]

Ip = lines[0]

Raspicode = lines[1]

# Send Data

Location = requests.get("http://" + Ip + "/assignLocation/" + Raspicode)

Location = Location.text

print(Location)

while True:

    CrdNumber = input()

    requests.post('http://' + Ip + '/rpisst', data = {'Id' : CrdNumber, 'Ort' : Location})
