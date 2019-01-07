import json

game_data_raw = open('/Users/sam.curtis@ibm.com/Desktop/code/nba/Spacing Analysis/GameDataSample.json')
game_data = json.load(game_data_raw)

cleansed_game_data = {}

cleansed_game_data['gameid'] = game_data['gameid']
cleansed_game_data['gamedate'] = game_data['gamedate']
cleansed_game_data['visitor'] = game_data['events'][0]['visitor']
cleansed_game_data['home'] = game_data['events'][0]['home']
cleansed_game_data['events'] = []

for event in game_data['events']:
    cleansed_game_data['events'].append({'eventId' : event['eventId'], 'moments' : event['moments']})

cleansed_json = json.dumps(cleansed_game_data)
fileName = cleansed_game_data['gamedate'] + '_' + cleansed_game_data['visitor']['abbreviation'] + '_' + cleansed_game_data['home']['abbreviation'] + '.json'

f = open(fileName,'w')
f.write(cleansed_json)
f.close()