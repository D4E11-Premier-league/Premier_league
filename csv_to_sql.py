import pymysql
import pandas as pd
from sqlalchemy import create_engine

# personal config
file_path = 'your git folder path'
user = "your username"
pw = "your password"



# create sql engine
client = pymysql.connect(
        host='localhost',
        user=user,
        password=pw,
        cursorclass=pymysql.cursors.DictCursor
    )

cursor = client.cursor()
cursor.execute('CREATE DATABASE Premier_league')
engine = create_engine(f"mysql+pymysql://{user}:{pw}@localhost/Premier_league")


# extract data
general = pd.read_csv(f'{file_path}/general.csv')
attack = pd.read_csv(f'{file_path}/attack_data.csv')
defence = pd.read_csv(f'{file_path}/denfence_data.csv')
goalkeeper = pd.read_csv(f'{file_path}/goalkeeper1.csv')
players_info = pd.read_csv(f'{file_path}/playersInfo.csv')

name = ['general','attack','defence','goalkeeper','players_info']
l = [general,attack,defence,goalkeeper,players_info]

# dump data
for i in range(len(l)):
    l[i].to_sql(name[i], con = engine, if_exists = 'append', index=False)
    print(name[i],' done!')