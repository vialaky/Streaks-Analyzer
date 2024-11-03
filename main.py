import sys
from collections import defaultdict, OrderedDict
import json
import pprint
from datetime import datetime

pp = pprint.PrettyPrinter(indent=4)


def read_data():

    with open('football.json-master/2010-11/at.1.json', 'r') as file:
        data = json.load(file)

    match_result = defaultdict(dict)
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

    return match_result


# pp.pprint(match_result)

teams_data = read_data()

for k, v in teams_data.items():
    teamchain_dict = OrderedDict(sorted(v.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'), reverse=False))
    teamchain_ls = [value for value in teamchain_dict.values()]
    print(k, teamchain_ls)
    # sys.exit()

# print(cnt)
# print(f'home: {home}   away: {away}   draws: {draws}')

# ordered_data = sorted(match_result.items(), key = lambda x:datetime.strptime(x[0], '%Y-%m-%d'), reverse=True)

# pp.pprint(ordered_data)
