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
table = 'position'
table = pd.read_csv(f'{file_path}/{table}.csv')

cursor.execute('CREATE DATABASE IF NOT EXISTS premier_league')
cursor.execute('DROP TABLE IF EXISTS premier_league.position')
cursor.execute('''
	CREATE TABLE IF NOT EXISTS premier_league.position (
		positionCategory VARCHAR(255),
		position VARCHAR(255) PRIMARY KEY
		)
	''')
for i in range(len(table)):
	cursor.execute(f'''
		INSERT INTO premier_league.position (
			`positionCategory`,
			`position`)
		VALUES (
			'{table['positionCategory'][i]}',
			'{table['position'][i]}'
			);
		''')
client.commit()
