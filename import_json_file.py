import json

with open('user_codes.json') as user_codes_file:
usercodess = json.load(user_codes_file)
for usercode in usercodes['usercodes']['usercode']:
    print('prefix', usercode['prefix'])
    print('description:', usercode['descrition'])
