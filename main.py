import itertools
from collections import defaultdict, OrderedDict
import json
import pprint
from datetime import datetime

pp = pprint.PrettyPrinter(indent=4)

folders = [
    'football.json-master/2010-11/',
    'football.json-master/2011-12/',
    'football.json-master/2012-13/',
    # 'football.json-master/2010-11/en.1.json',
    # 'football.json-master/2010-11/en.2.json',
    # 'football.json-master/2010-11/en.3.json',
    # 'football.json-master/2010-11/en.4.json',

]

files = [
    'at.1.json',
    'at.2.json',
    'de.1.json',
    'de.2.json',
    'en.1.json',
    'en.2.json',
    'en.3.json',
    'en.4.json',
    'es.1.json',
    'es.2.json',
]


# paths = [
#     'football.json-master/2010-11/at.1.json',
#     'football.json-master/2010-11/at.2.json',
#     'football.json-master/2010-11/de.1.json',
#     'football.json-master/2010-11/en.1.json',
#     'football.json-master/2010-11/en.2.json',
#     'football.json-master/2010-11/en.3.json',
#     'football.json-master/2010-11/en.4.json',
#
# ]

match_result = defaultdict(dict)


def read_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

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


for folder in folders:
    for file in files:
        try:
            teams_data = read_data(folder + file)
        except FileNotFoundError:
            pass

series = []

for k, v in teams_data.items():
    teamchain_dict = OrderedDict(
        sorted(v.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'), reverse=False))
    teamchain_ls = [value for value in teamchain_dict.values()]
    for item, group in itertools.groupby(teamchain_ls):
        streak = len(list(group))

        if streak > 2:
            series.append((item, streak))

# print(cnt)
# print(f'home: {home}   away: {away}   draws: {draws}')


streaks_count = defaultdict(dict)
streaks_success = defaultdict(dict)
streaks = defaultdict(dict)

for item in series:
    print(item)
    result = item[0]
    val = item[1]

    while 3 <= val <= item[1]:

        try:
            streaks_count[result][val] += 1
        except KeyError:
            streaks_count[result][val] = 1

        if val < item[1]:

            try:
                streaks_success[result][val] += 1
            except KeyError:
                streaks_success[result][val] = 1

        try:
            streaks[result][
                val] = f'{round(streaks_success[result][val] / streaks_count[result][val] * 100)}% for {streaks_count[result][val]}'
        except KeyError:
            streaks[result][val] = 0

        val -= 1

print('Count:')
pp.pprint(streaks_count)
print('================')
print('Success:')
pp.pprint(streaks_success)
print('================')
print('================')

print('Summary:')
pp.pprint(streaks)
print(f'Total streaks: {len(series)}')
