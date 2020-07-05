
import requests
import pandas as pd
import json
from functools import reduce
import time

attributes = {
    'general' : ['goals','goal_assist','appearances','mins_played','yellow_card','red_card','total_sub_on','total_sub_off'],
    'attack' : ['total_scoring_att', 'ontarget_scoring_att', 'hit_woodwork', 'att_hd_goal', 'att_pen_goal', 'att_freekick_goal', 'total_offside', 'touches', 'total_pass', 'total_through_ball', 'total_cross', 'corner_taken'],
    'defence' : ['outfielder_block','interception','total_tackle','last_man_tackle','total_clearance','head_clearance','aerial_won','own_goals','error_lead_to_goal','penalty_conceded','fouls','aerial_lost'],
    'goalkeeper' : ['clean_sheet','goals_conceded','saves','penalty_save','punches','total_high_claim','total_keeper_sweeper','keeper_throws','goal_kicks']
}

folder_path = '' #'your git folder path'


def flatten(d): # full stackoverflow được đoạn code dùng recursion hay lắm, dùng để làm phẳng mấy cái nested dict
    out = {}
    for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                deeper = flatten(subdict).items()
                out.update({key + '_' + key2: val2 for key2, val2 in deeper})
        else:
            out[key] = val
    return out

def surfing_the_web(crit,page_size=1000):
    url = f'https://footballapi.pulselive.com/football/stats/ranked/players/{criteria}?page=0&pageSize={page_size}&compSeasons=274&comps=1&compCodeForActivePlayer=EN_PR&altIds=true'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36',
              'authority': 'footballapi.pulselive.com',
              'method': 'GET',
              'path': f'/football/stats/ranked/players/{criteria}?page=0&pageSize={page_size}&compSeasons=274&comps=1&compCodeForActivePlayer=EN_PR&altIds=true',
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
    data = json.loads(r.text)
    return data

playersInfo = []
for key in attributes:
    for y in range(len(attributes[key])):
        t = time.process_time()
        criteria = attributes[key][y]
        l = []
        data  = surfing_the_web(criteria)
        for i in range(len(data['stats']['content'])):
            l.append([data['stats']['content'][i]['owner']['playerId'],data['stats']['content'][i]['value']])
            player = flatten(data['stats']['content'][i]['owner'])
            playersInfo.append(player)
        exec(f"{criteria} = pd.DataFrame(l,columns = ['player_id','{criteria}'])")
        print(f'crawling {key} {attributes[key][y]} in',round(time.process_time()-t,2),'s')
    df = [eval(x) for x in attributes[key]]
    df = reduce(lambda x, y: pd.merge(x, y, left_on = 'player_id',right_on = 'player_id', how = 'outer'), df).fillna(0)
    exec(f'{key}=df')
    df.to_csv(f'{folder_path}/{key}_data.csv',index = False)

playersInfo = pd.DataFrame(playersInfo).drop_duplicates('playerId').reset_index(drop = True)

col = ['nationalTeam_demonym','active','birth_date_millis', 'currentTeam_club_name','currentTeam_club_abbr', 'currentTeam_teamType','currentTeam_shortName', 'currentTeam_id', 'currentTeam_altIds_opta','birth_country_demonym', 'birth_place', 'age', 'name_first', 'name_last', 'id', 'altIds_opta', 'name_middle']
playersInfo = playersInfo.drop(columns = col)

col = ['playerId', 'info_shirtNum','info_loan', 'nationalTeam_isoCode', 'nationalTeam_country','currentTeam_name', 'currentTeam_club_id', 'birth_date_label', 'birth_country_isoCode','birth_country_country', 'name_display']
position = playersInfo.drop(columns = col).drop_duplicates('info_positionInfo').reset_index(drop = True)
col = ['playerId', 'info_position', 'info_shirtNum', 'info_positionInfo','info_loan', 'nationalTeam_isoCode', 'nationalTeam_country','birth_date_label', 'birth_country_isoCode','birth_country_country', 'name_display']
club = playersInfo.drop(columns = col).drop_duplicates('currentTeam_club_id').reset_index(drop = True)
col = ['playerId', 'info_position', 'info_shirtNum', 'info_positionInfo','info_loan', 'nationalTeam_isoCode', 'nationalTeam_country','currentTeam_name', 'currentTeam_club_id', 'birth_date_label', 'name_display']
birth_country = playersInfo.drop(columns = col).drop_duplicates('birth_country_isoCode').reset_index(drop = True)
birth_country.columns = ['country_code','country_name']
col = ['playerId', 'info_position', 'info_shirtNum', 'info_positionInfo','info_loan','currentTeam_name', 'currentTeam_club_id', 'birth_date_label','birth_country_isoCode', 'birth_country_country', 'name_display']
nationalTeam = playersInfo.drop(columns = col).drop_duplicates('nationalTeam_isoCode').reset_index(drop = True)
nationalTeam.columns = ['country_code','country_name']
country = pd.concat([birth_country,nationalTeam]).drop_duplicates('country_code')
playersInfo = playersInfo.drop(columns = ['info_position','nationalTeam_country','currentTeam_name', 'birth_country_country'])

position.to_csv(f'{folder_path}/position.csv',index = False)
club.to_csv(f'{folder_path}/club.csv',index = False)
country.to_csv(f'{folder_path}/country.csv',index = False)
playersInfo.to_csv(f'{folder_path}/players_info.csv',index = False)
