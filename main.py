import json

with open('football.json-master/2010-11/at.1.json', 'r') as file:
    data = json.load(file)

for item in data['rounds']:
    match = item['matches'][0]
    print(match)
