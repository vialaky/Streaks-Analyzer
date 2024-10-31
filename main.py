import collections
import json
import pprint

with open('football.json-master/2010-11/at.1.json', 'r') as file:
    data = json.load(file)

match_result = collections.defaultdict(dict)
# match_result = {}
pp = pprint.PrettyPrinter(indent=4)


cnt = home = away = draws = 0

for rounds in data['rounds']:
    for match in rounds['matches']:
        # print(match)
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

        except:
            pass
        # print('===')

# for item in data['rounds']:
#     match = item['matches']
#
#     print(match)
#
        # try:
        #     result = match['score']
        #
        #     if result['ft'][0] > result['ft'][1]:
        #         match_result[match['team1']]['date'] = match['date']
        #         match_result[match['team1']]['result'] = 'win'
        #
        #         match_result[match['team2']]['date'] = match['date']
        #         match_result[match['team2']]['result'] = 'lose'
        #
        #     elif result['ft'][0] < result['ft'][1]:
        #         match_result[match['team1']]['date'] = match['date']
        #         match_result[match['team1']]['result'] = 'lose'
        #
        #         match_result[match['team2']]['date'] = match['date']
        #         match_result[match['team2']]['result'] = 'win'
        #
        #     else:
        #         match_result[match['team1']]['date'] = match['date']
        #         match_result[match['team1']]['result'] = 'draw'
        #
        #         match_result[match['team2']]['date'] = match['date']
        #         match_result[match['team2']]['result'] = 'draw'
        #
        # except KeyError:
        #     pass
#
# for k, v in match_result.items():
#     print(k, v)

pp.pprint(match_result)

# for team in match_result.keys():
#     print(team)
#     for v in match_result.values():
#         print(v)

print(cnt)
print(f'home: {home}   away: {away}   draws: {draws}')

# print(collections.Counter(map(lambda student: student['win'], match_result))

# unique_values = len({element for sublist in match_result.values() for element in sublist})
# print(unique_values)

# # В обращении с вложенными структурами Python показывает свою мощь
# nested_dict = {'a': [1, 2], 'b': [2, 3], 'c': [3, 4]}
#
# # Множества помогают избежать дубликатов, а len() помогает их подсчитать
# unique_values = len({element for sublist in nested_dict.values() for element in sublist})
#
# print(unique_values)