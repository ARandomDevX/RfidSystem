import requests


# Config

lines = [line.rstrip('\n') for line in open('config.txt')]

Ip = lines[0]

Location = lines[1]

# Send Data

while True:

    CrdNumber = input()

    requests.post('https://' + Ip + '/raspberrypi', data = {'Id' : CrdNumber, 'Ort' : Location})
