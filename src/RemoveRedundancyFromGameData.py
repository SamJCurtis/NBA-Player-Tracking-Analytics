#!/usr/bin/python
import json
import sys


#removes redudant entries for 'home' and 'visitor' and returns a new dictionary w/ the cleansed data
def removeDuplicateTeamInformation(fileName):
    #load the raw json data
    game_data_raw = open(fileName)
    game_data = json.load(game_data_raw)

    #create a new dictionary which will only store the home and visitor information once
    cleansed_game_data = {}

    #the gameid and gamedate are the same
    cleansed_game_data['gameid'] = game_data['gameid']
    cleansed_game_data['gamedate'] = game_data['gamedate']

    #we now have keys for the visitor and home team at the top level of the json
    #we can just grab these from the first event as they are the same for every event
    cleansed_game_data['visitor'] = game_data['events'][0]['visitor']
    cleansed_game_data['home'] = game_data['events'][0]['home']

    #create a blank list for storing the events without the home and visitor data attached to each one 
    cleansed_game_data['events'] = []

    #for each event, we now only want the eventId and the list of moments
    for event in game_data['events']:
        cleansed_game_data['events'].append({'eventId' : event['eventId'], 'moments' : event['moments']})

    return cleansed_game_data

#filename is passed in via the command line when the script is run (google Python command line arguments for more information
cleansed_game_data = removeDuplicateTeamInformation(sys.argv[1])

#create a filename from the specific game data
fileName = cleansed_game_data['gamedate'] + '_' + cleansed_game_data['visitor']['abbreviation'] + '_' + cleansed_game_data['home']['abbreviation'] + '.json'

#convert dictionary to json and write to file 
cleansed_json = json.dumps(cleansed_game_data,separators=(',', ':'))
f = open(fileName,'w')
f.write(cleansed_json)
f.close()