# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:53:31 2020

@author: Tung Linh
"""
import requests
import pandas as pd
import json
from functools import reduce

criteria = [
    'goals',
    'goal_assist',
    'appearances',
    'mins_played',
    'yellow_card',
    'red_card',
    'total_sub_on',
    'total_sub_off'
    ]
season_num = [274,210,79,54,42,27,22,21,20,19,18,17,16,15,14,13,12,11,10]
x = 0 #season_num
page_size = 1000
page_num = 0

# general information:
for y in range(1):
    l = []
    url = f'https://footballapi.pulselive.com/football/stats/ranked/players/{criteria[y]}?page={page_num}&pageSize={page_size}&compSeasons={season_num[x]}&comps=1&compCodeForActivePlayer=EN_PR&altIds=true'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36',
              'authority': 'footballapi.pulselive.com',
              'method': 'GET',
              'path': f'/football/stats/ranked/players/{criteria[y]}?page={page_num}&pageSize={page_size}&compSeasons={season_num[x]}&comps=1&compCodeForActivePlayer=EN_PR&altIds=true',
              'scheme': 'https',
              'accept': '*/*',
              'accept-encoding': 'gzip, deflate, br',
              'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
              'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'origin': 'https://www.premierleague.com',
              'referer': 'https://www.premierleague.com/stats/top/players/goals',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'cross-site'}
    r = requests.get(url,headers = headers)
    print(f'crawling {criteria[y]} done!')
    data = json.loads(r.text)
    for i in range(len(data['stats']['content'])):
        l.append([data['stats']['content'][i]['owner']['playerId'],data['stats']['content'][i]['value']])
    exec(f"{criteria[y]} = pd.DataFrame(l,columns = ['player_id','{criteria[y]}'])")
# =============================================================================
# general = [goals,goal_assist,appearances,mins_played,yellow_card,red_card,total_sub_on,total_sub_off]
# general = reduce(lambda x, y: pd.merge(x, y, left_on = 'player_id',right_on = 'player_id', how = 'outer'), general)
# general = general.fillna(0)
# general.to_csv('C:/Users/Tung Linh/Desktop/D4E/general.csv',index = False)
# =============================================================================

# player information
page_size = 30
page_num = 49
l = []
for num in range(page_num):
    url = f'https://footballapi.pulselive.com/football/players?pageSize={page_size}&compSeasons=274&altIds=true&page={num}&type=player&id=-1&compSeasonId=274'
    headers = {
        'authority': 'footballapi.pulselive.com',
        'method': 'GET',
        'path': f'/football/players?pageSize={page_size}&compSeasons=274&altIds=true&page={num}&type=player&id=-1&compSeasonId=274',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.premierleague.com',
        'referer': 'https://www.premierleague.com/players',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36'
        }
    
    r = requests.get(url,headers = headers)
    print(f'crawling players page {num} done!')
    data = json.loads(r.text)
    print(len(data['content']))
    for i in range(len(data['content'])):
        place = None
        shirtNum = None
        date = None
        nationalId = None
        national = None
        country = None
        if 'currentTeam' in data['content'][i]:
            clubId = data['content'][i]['currentTeam']['club']['id']
            clubName = data['content'][i]['currentTeam']['club']['name']
        else:
            clubId = data['content'][i]['previousTeam']['club']['id']
            clubName = data['content'][i]['previousTeam']['club']['name'] + ' (previousTeam)'
        if 'shirtNum' in data['content'][i]['info']:
            shirtNum = data['content'][i]['info']['shirtNum']
        if 'date' in data['content'][i]['birth']:
            date = data['content'][i]['birth']['date']['label']
        if 'country' in data['content'][i]['nationalTeam']:
            national = data['content'][i]['nationalTeam']['country']
        if 'isoCode' in data['content'][i]['nationalTeam']:
            nationalId = data['content'][i]['nationalTeam']['isoCode']
        l.append([
         data['content'][i]['playerId'],
         data['content'][i]['name']['first'],
         data['content'][i]['name']['last'],
         shirtNum,
         data['content'][i]['info']['position'],
         data['content'][i]['info']['positionInfo'],
         clubId,
         clubName,
         nationalId,
         national,
         date
         ])

col = [
 'playerId',
 'first_name',
 'last_name',
 'shirtNum',
 'position',
 'positionInfo',
 'teamId',
 'teamName',
 'nationalTeamId',
 'nationalTeamName',
 'birthDate'
 ]
playersInfo = pd.DataFrame(l, columns = col)
playersInfo.to_csv('C:/Users/Tung Linh/Desktop/D4E/playersInfo.csv',index = False)