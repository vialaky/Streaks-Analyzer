from collections import defaultdict
import json
import pprint

with open('football.json-master/2010-11/at.1.json', 'r') as file:
    data = json.load(file)

match_result = defaultdict(dict)
pp = pprint.PrettyPrinter(indent=4)

cnt = home = away = draws = 0

for rounds in data['rounds']:
    for match in rounds['matches']:
        cnt += 1

        try:
            if match['score']['ft'][0] > match['score']['ft'][1]:
                match_result[match['team1']][match['date']] = 'win'
                match_result[match['team2']][match['date']] = 'lose'
                home += 1

            elif match['score']['ft'][0] < match['score']['ft'][1]:
                match_result[match['team1']][match['date']] = 'lose'
                match_result[match['team2']][match['date']] = 'win'
                away += 1

            else:
                match_result[match['team1']][match['date']] = 'draw'
                match_result[match['team2']][match['date']] = 'draw'
                draws += 1

        except KeyError:
            pass

pp.pprint(match_result)

print(cnt)
print(f'home: {home}   away: {away}   draws: {draws}')
