import requests


# Config

lines = [line.rstrip('\n') for line in open('config.txt')]

Ip = lines[0]

Raspicode = lines[1]

# Send Data

Location = requests.get("http://" + Ip + "/assignLocation/" + Raspicode)

print(Location)

while True:

    CrdNumber = input()

    requests.post('https://' + Ip + '/raspberrypi', data = {'Id' : CrdNumber, 'Ort' : Location})
