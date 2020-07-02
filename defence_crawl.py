import requests
import pandas as pd
import json
from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.get_database('PremierLeague')
collection = db.get_collection('Premier_Defence')
player_id_collection = db.get_collection('Player_id')
criteria = [
    'outfielder_block',
    'interception',
    'total_tackle',
    'last_man_tackle',
    'total_clearance',
    'head_clearance',
    'aerial_won',
    'own_goals',
    'error_lead_to_goal',
    'penalty_conceded',
    'fouls',
    'aerial_lost'
    ]


#lay data defence----------------------------


# for i in range(12):
#     url = f'https://footballapi.pulselive.com/football/stats/ranked/players/{criteria[i]}?page=0&pageSize=1000&compSeasons=274&comps=1&compCodeForActivePlayer=EN_PR&altIds=true'
#     headers = {
#         'authority': 'footballapi.pulselive.com',
#         'method': 'GET',
#         'path': f'/football/players?pageSize=0&compSeasons=274&altIds=true&page=1000&type=player&id=-1&compSeasonId=274',
#         'scheme': 'https',
#         'accept': '*/*',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'origin': 'https://www.premierleague.com',
#         'referer': 'https://www.premierleague.com/stats/top/players/{criteria[i]}',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'cross-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36'
#         }
#     r = requests.get(url,headers = headers)
#     print(f'crawling {criteria[y]} done!')
#     data = json.loads(r.text)
#     collection.insert_one(data)

# lay toan bo player ID--------------------------------------------

# page_size = 30
# page_num = 49

# for num in range(page_num):
#     url = f'https://footballapi.pulselive.com/football/players?pageSize={page_size}&compSeasons=274&altIds=true&page={num}&type=player&id=-1&compSeasonId=274'
#     headers = {
#         'authority': 'footballapi.pulselive.com',
#         'method': 'GET',
#         'path': f'/football/players?pageSize={page_size}&compSeasons=274&altIds=true&page={num}&type=player&id=-1&compSeasonId=274',
#         'scheme': 'https',
#         'accept': '*/*',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'origin': 'https://www.premierleague.com',
#         'referer': 'https://www.premierleague.com/players',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'cross-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36'
#         }
    
    # r = requests.get(url,headers = headers)
    # data_id = json.loads(r.text)
    # for i in range(len(data_id['content'])):
    #     player_id_collection.insert_one(
    #         {
    #             'id' : data_id['content'][i]['playerId'],
    #             'outfielder_block' : 0,
    #             'interception' : 0,
    #             'total_tackle' : 0,
    #             'last_man_tackle' : 0,
    #             'total_clearance' : 0,
    #             'head_clearance' : 0,
    #             'aerial_won' : 0,
    #             'own_goals' : 0,
    #             'error_lead_to_goal' : 0,
    #             'penalty_conceded' : 0,
    #             'fouls' : 0,
    #             'aerial_lost' : 0
    #         }
    #     )
#===========================================================================
# dong bo du lieu tu data defence toi player ID


# for player in collection.find():
#     for j in range(len(player['stats']['content'])):
#         query = {'id' : player['stats']['content'][j]['owner']['playerId'] }
#         update =  {
#             '$set': {
#                 player['stats']['content'][j]['name']:player['stats']['content'][j]['value']
#             }
#         }
#         player_id_collection.update(query,update)

#convert ra file csv----------------------------------------------

# final = []
# player  = player_id_collection.find()
# for i in player:
#     final.append([i['id'],i['outfielder_block'],i['interception'],i['total_tackle'],i['last_man_tackle'],i['total_clearance'],i['head_clearance'],i['aerial_won'],i['own_goals'],i['error_lead_to_goal'],i['penalty_conceded'],i['fouls'],i['aerial_lost']])
# col = ['player_id',
#     'outfielder_block',
#     'interception',
#     'total_tackle',
#     'last_man_tackle',
#     'total_clearance',
#     'head_clearance',
#     'aerial_won',
#     'own_goals',
#     'error_lead_to_goal',
#     'penalty_conceded',
#     'fouls',
#     'aerial_lost'
# ]
# defence = pd.DataFrame(final, columns = col)
# =============================================================================
defence.to_csv('C:/Users/ADMIN/Desktop/denfence.csv',index = False)

    