import itertools
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

series = []

for k, v in teams_data.items():
    teamchain_dict = OrderedDict(
        sorted(v.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'), reverse=False))
    teamchain_ls = [value for value in teamchain_dict.values()]
    # print(k)
    for item, group in itertools.groupby(teamchain_ls):
        streak = len(list(group))

        if streak > 2:
            # print(f'{item} - {seria}')
            series.append((item, streak))

    # print(series)

    # print()
    # print(k, teamchain_ls)

    # sys.exit()

# print(cnt)
# print(f'home: {home}   away: {away}   draws: {draws}')

# ordered_data = sorted(match_result.items(), key = lambda x:datetime.strptime(x[0], '%Y-%m-%d'), reverse=True)

# pp.pprint(ordered_data)

# print(series)


streaks_count = defaultdict(dict)
streaks_success = defaultdict(dict)
streaks = defaultdict(dict)
# win = defaultdict(dict)
# lose = defaultdict(dict)

for item in series:
    print(item)
    result = item[0]
    val = item[1]

    while 3 <= val <= item[1]:
        # print(val)

        try:
            streaks_count[result][val] += 1
        except KeyError:
            # pass
            streaks_count[result][val] = 1

        if val < item[1]:
        #     streaks_success[result][val] = 0
        # else:
            try:
                streaks_success[result][val] += 1
            except KeyError:
                streaks_success[result][val] = 1

        try:
            streaks[result][val] = f'{round(streaks_success[result][val] / streaks_count[result][val] * 100)}%'
        except KeyError:
            streaks[result][val] = 0
        # try:
        #     streaks_count[result][val]['success'] += 1
        #
        # except KeyError as e:
        #     # print(e)
        #     streaks_count[result][val]['success'] = 1

        # try:
        #     streaks_count[result][val]['cnt'] += 1
        # except KeyError:
        #     streaks_count[result][val]['cnt'] = 1

        val -= 1

print('Count:')
pp.pprint(streaks_count)
print('================')
print('Success:')
pp.pprint(streaks_success)
print('================')
print('================')
#
# for k in streaks_count.keys():
#     streaks[]

print('Summary:')
pp.pprint(streaks)
print(f'Total streaks: {len(series)}')
