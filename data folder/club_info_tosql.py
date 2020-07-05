import pymysql
import pandas as pd

# personal config
file_path = 'C:/Users/Tung Linh/Desktop/D4E_premier_league/data folder' #'your git folder path'
user = 'root' #"your username"
pw = 'Nsi668888' #"your password"

# create sql engine
client = pymysql.connect(
        host='localhost',
        user=user,
        password=pw,
        cursorclass=pymysql.cursors.DictCursor)

cursor = client.cursor()
table = 'club_info'
table = pd.read_csv(f'{file_path}/{table}.csv')

cursor.execute('CREATE DATABASE IF NOT EXISTS premier_league')
cursor.execute('''
   CREATE TABLE IF NOT EXISTS premier_league.club_info (
       clubId INT(11) PRIMARY KEY, 
       clubName VARCHAR(255), 
       city VARCHAR(255), 
       ground VARCHAR(255), 
       groundCapacity INT(11),
       groundLatitude DECIMAL(15,8), 
       groundLongitude DECIMAL(15,8), 
       homeWins INT(11), 
       homeDraws INT(11),
       homeLoses INT(11), 
       awayWins INT(11), 
       awayDraws INT(11), 
       awayLoses INT(11), 
       possesions DECIMAL(10,8),
       passAccuracy DECIMAL(10,8)
       )
   ''')

for i in range(len(table)):
	cursor.execute(f'''
		INSERT INTO premier_league.club_info (
			`clubId`,
			`clubName`,
			`city`,
			`ground`,
			`groundCapacity`,
			`groundLatitude`,
			`groundLongitude`,
			`homeWins`,
			`homeDraws`,
			`homeLoses`,
			`awayWins`,
			`awayDraws`,
			`awayLoses`,
			`possesions`,
			`passAccuracy`)
        VALUES (
			{table['clubId'][i]},
			'{table['clubName'][i]}',
			'{table['city'][i]}',
			'{table['ground'][i]}',
			{table['groundCapacity'][i]},
			{table['groundLatitude'][i]},
			{table['groundLongitude'][i]},
			{table['homeWins'][i]},
			{table['homeDraws'][i]},
			{table['homeLoses'][i]},
			{table['awayWins'][i]},
			{table['awayDraws'][i]},
			{table['awayLoses'][i]},
			{table['possesions'][i]},
			{table['passAccuracy'][i]}
			);
		''')
client.commit()
