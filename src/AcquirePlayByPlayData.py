import pandas as pd
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

def acquire_gameData(gameid):
    header_data = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Host': 'stats.nba.com',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
                }

    game_url = 'http://stats.nba.com/stats/playbyplayv2?EndPeriod=0&EndRange=0&GameID='+gameid+\
                '&RangeType=0&StartPeriod=0&StartRange=0' #address for querying the data
    response = requests.get(game_url,headers = header_data, timeout=5) #go get the data
    headers = response.json()['resultSets'][0]['headers'] #get headers of data
    gameData = response.json()['resultSets'][0]['rowSet'] #get actual data from json object
    df = pd.DataFrame(gameData, columns=headers) #turn the data into a pandas dataframe
    df = df[[df.columns[1], df.columns[2],df.columns[7],df.columns[9],df.columns[18]]] #there's a ton of data here, so I trim  it doown
    df['TEAM'] = df['PLAYER1_TEAM_ABBREVIATION']
    df = df.drop('PLAYER1_TEAM_ABBREVIATION', 1)
    return df


