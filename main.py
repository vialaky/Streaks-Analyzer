import json

with open('football.json-master/2010-11/at.1.json', 'r') as file:
    data = json.load(file)

print(data)