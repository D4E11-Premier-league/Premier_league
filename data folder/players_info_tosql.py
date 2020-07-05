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
table = 'players_info'
table = pd.read_csv(f'{file_path}/{table}.csv')

cursor.execute('CREATE DATABASE IF NOT EXISTS premier_league')
cursor.execute('DROP TABLE IF EXISTS premier_league.players_info')
cursor.execute('''
	CREATE TABLE IF NOT EXISTS premier_league.players_info (
		playerId INT(11) PRIMARY KEY,
		shirtNum INT(11),
		positionInfo VARCHAR(255),
		loan VARCHAR(255),
		nationalTeamId VARCHAR(255),
		currentTeamId INT(11),
		birth VARCHAR(255),
		birthCountryId VARCHAR(255),
		playerName VARCHAR(255),
        FOREIGN KEY (positionInfo) REFERENCES premier_league.position(position),
        FOREIGN KEY (nationalTeamId) REFERENCES premier_league.country(countryId),
        FOREIGN KEY (birthCountryId) REFERENCES premier_league.country(countryId),
        FOREIGN KEY (currentTeamId) REFERENCES premier_league.club_info(clubId)
		)
	''')
for i in range(len(table)):
	cursor.execute(f'''
		INSERT INTO premier_league.players_info (
			`playerId`,
			`shirtNum`,
			`positionInfo`,
			`loan`,
			`nationalTeamID`,
			`currentTeamId`,
			`birth`,
			`birthCountryId`,
			`playerName`)
		VALUES (
			{table['playerId'][i]},
			{table['shirtNum'][i]},
			'{table['positionInfo'][i]}',
			'{table['loan'][i]}',
			'{table['nationalTeamID'][i]}',
			{table['currentTeamId'][i]},
			'{table['birth'][i]}',
			'{table['birthCountryId'][i]}',
			'{table['playerName'][i]}'
			);
		''')
client.commit()
